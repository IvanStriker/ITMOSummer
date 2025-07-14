from django.shortcuts import render
from django.http import HttpResponseRedirect
from random import choice
from general.models import User, Problem, Answer, PupilToProblem

def cUser(request):
    return User.objects.get(id=request.session["user"])


def checkRight(request, level=0):
    if "user" not in request.session:
        return -1
    user = cUser(request)
    if user.isAdmin >= level:
        return user
    else:
        return -1


def index(request):
    return render(request, 'index.html', {})


def registerForm(request):
    return render(request, 'registerForm.html', {})


def enterForm(request):
    return render(request, 'enterForm.html', {})


def register(request):
    if request.method == "POST":
        (post := request.POST.dict()).pop("csrfmiddlewaretoken")
        if len(User.objects.filter(login=post["login"]).values()) > 0:
            return HttpResponseRedirect("/reg/")
        request.session["user"] = User.objects.create(isAdmin=0, **post).id
    return HttpResponseRedirect("/personal")


def enter(request):
    if request.method == "POST":
        (post := request.POST.dict()).pop("csrfmiddlewaretoken")
        request.session["user"] = User.objects.get(**post).id
    return HttpResponseRedirect("/personal")


def personal(request):
    user = checkRight(request, 0)
    if user == -1:
        return HttpResponseRedirect("/enter/")
    if user.isAdmin == 1:
        return render(request, 'personalAdmin.html', {"user": user})
    else:
        return render(request, 'personalPupil.html', {"user": user})


def createProblemForm(request):
    user = checkRight(request, 1)
    if user == -1:
        return render(request, 'enterForm.html', {})
    return render(request, 'createProblemForm.html', {})


def createProblem(request):
    user = checkRight(request, 1)
    if user == -1:
        return HttpResponseRedirect("/enter/")
    if request.method == "POST":
        (post := request.POST.dict()).pop("csrfmiddlewaretoken")
        prob = user.problem_set.create(title=post["title"], description=post["description"])
        post.pop("title"), post.pop("description")
        for ans in post:
            prob.answer_set.create(text=post[ans], problem=prob)
    return HttpResponseRedirect("/personal/problem_list/")


def problemList(request):
    user = checkRight(request, 0)
    if user == -1:
        return HttpResponseRedirect("/enter/")
    if user.isAdmin:
        return render(request, 'problemList.html', {"problems": user.problem_set.filter(archived=0).values()})
    else:
        ids = PupilToProblem.objects.filter(pupilID=user.id).values_list("problemID", flat=True)
        ids = set(ids)
        return render(request, 'problemListPupil.html', {"problems": Problem.objects.filter(id__in=ids).values()})


def sendList(request):
    user = checkRight(request, 1)
    if user == -1:
        return HttpResponseRedirect("/enter/")
    if request.method == "POST":
        (post := request.POST.dict()).pop("csrfmiddlewaretoken")
        for prob in post:
            user.problem_set.filter(id=int(prob)).update(archived=1, awaitsPupil=1)
    return HttpResponseRedirect("/personal")


def getProblem(request):
    user = checkRight(request, 0)
    if user == -1:
        return HttpResponseRedirect("/enter/")
    problemsToSolve = Problem.objects.filter(awaitsPupil=1).values()
    if len(problemsToSolve) > 0:
        prob = choice(Problem.objects.filter(awaitsPupil=1).values())
        Problem.objects.filter(id=prob["id"]).update(awaitsPupil=0)
        PupilToProblem.objects.create(pupilID=user.id, problemID=prob["id"])
    return HttpResponseRedirect("/personal")



def editProblemForm(request, id):
    user = checkRight(request, 1)
    if user == -1:
        return HttpResponseRedirect("/enter/")
    return render(request, 'editProblemForm.html', {"problem": user.problem_set.get(id=id)})


def editProblem(request, id):
    user = checkRight(request, 1)
    if user == -1:
        return HttpResponseRedirect("/enter/")
    if request.method == "POST":
        (post := request.POST.dict()).pop("csrfmiddlewaretoken")
        prob = user.problem_set.get(id=id)
        prob.title = post["title"]
        prob.description = post["description"]
        post.pop("title"), post.pop("description")
        for ans in prob.answer_set.values():
            prob.answer_set.get(id=ans["id"]).delete()
        for ans in post:
            prob.answer_set.create(text=post[ans], problem=prob)
        prob.save()
    return HttpResponseRedirect("/personal/problem_list/")


def deleteProblem(request, id):
    user = checkRight(request, 1)
    if user == -1:
        return HttpResponseRedirect("/enter/")
    user.problem_set.get(id=id).delete()
    return HttpResponseRedirect("/personal/problem_list/")


def archive(request):
    user = checkRight(request, 1)
    if user == -1:
        return HttpResponseRedirect("/enter/")
    return render(request, 'archive.html', {"problems": user.problem_set.filter(archived=1).values()})


def clearArchive(request):
    user = checkRight(request, 1)
    if user == -1:
        return HttpResponseRedirect("/enter/")
    user.problem_set.filter(archived=1).delete()
    return HttpResponseRedirect("/personal/archive/")


def problemInfo(request, id):
    user = checkRight(request, 1)
    if user == -1:
        return HttpResponseRedirect("/enter/")
    return render(request, 'problemInfo.html', {"problem": user.problem_set.get(id=id)})


def solveForm(request, id):
    user = checkRight(request, 0)
    if user == -1:
        return HttpResponseRedirect("/enter/")
    return render(request, 'solve.html', {"problem": Problem.objects.get(id=id)})


def solve(request):
    user = checkRight(request, 0)
    if user == -1:
        return HttpResponseRedirect("/enter/")
    if request.method == "POST":
        (post := request.POST.dict()).pop("csrfmiddlewaretoken")
        PupilToProblem.objects.get(pupilID=user.id, problemID=int(post["problemId"])).delete()
        Problem.objects.filter(id=int(post["problemId"])).update(solved=1)
    return HttpResponseRedirect("/personal/problem_list/")


def settings(request):
    user = checkRight(request, 0)
    if user == -1:
        return HttpResponseRedirect("/enter/")
    return render(request, 'settings.html', {"user": user})


def setSettings(request):
    user = checkRight(request, 0)
    if user == -1:
        return HttpResponseRedirect("/enter/")
    if request.method == "POST":
        (post := request.POST.dict()).pop("csrfmiddlewaretoken")
        User.objects.filter(id=user.id).update(**post)
        user = User.objects.get(id=user.id)
    return HttpResponseRedirect("/personal")


def myexit(request):
    user = checkRight(request, 0)
    if user == -1:
        return HttpResponseRedirect("/enter/")
    del request.session["user"]
    return HttpResponseRedirect("/enter/")

def deleteAccount(request):
    user = checkRight(request, 0)
    if user == -1:
        return HttpResponseRedirect("/enter/")
    PupilToProblem.objects.filter(pupilID=user.id).delete()
    User.objects.get(id=user.id).delete()
    return HttpResponseRedirect("/reg/")
