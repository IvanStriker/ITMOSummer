from django.db import models


class User(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    isAdmin = models.BooleanField(default=0)


class Problem(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    archived = models.BooleanField(default=0)
    awaitsPupil = models.BooleanField(default=0)
    solved = models.BooleanField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)


class Answer(models.Model):
    text = models.TextField()
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, default=None)


class PupilToProblem(models.Model):
    pupilID = models.IntegerField()
    problemID = models.IntegerField()
