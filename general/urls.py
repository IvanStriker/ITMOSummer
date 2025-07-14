from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reg/', views.registerForm, name='registerForm'),
    path('enter/', views.enterForm, name='enterForm'),
    path('reg/create', views.register, name='register'),
    path('enter/do', views.enter, name='enter'),
    path('personal', views.personal, name='personal'),
    path('personal/new_problem/', views.createProblemForm, name='createProblemForm'),
    path('personal/new_problem/create', views.createProblem, name='createProblem'),
    path('personal/problem_list/', views.problemList, name='problemList'),
    path('personal/problem_list/send', views.sendList, name='sendList'),
    path('personal/edit_problem/<int:id>', views.editProblemForm, name='editProblemForm'),
    path('personal/del_problem/<int:id>', views.deleteProblem, name='deleteProblem'),
    path('personal/edit_problem/do/<int:id>', views.editProblem, name='editProblem'),
    path('personal/archive/', views.archive, name='archive'),
    path('personal/archive/clear/', views.clearArchive, name='clearArchive'),
    path('personal/problem_info/<int:id>', views.problemInfo, name='problemInfo'),
    path('personal/solve/<int:id>', views.solveForm, name='solveForm'),
    path('personal/solve/do', views.solve, name='solve'),
    path('personal/settings/', views.settings, name='settings'),
    path('personal/settings/set', views.setSettings, name='setSettings'),
    path('personal/out/', views.myexit, name='myexit'),
    path('personal/get_problem/', views.getProblem, name='getProblem'),
    path('personal/delete_account/', views.deleteAccount, name='deleteAccount'),
]
