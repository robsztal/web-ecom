from django.shortcuts import render
from django.http import HttpResponse
from .models import Storage, Product
from .templates.main import *


def index(response, id):
    ls = Storage.objects.get(id=id)
    return HttpResponse("<h1>%s</h1>" % ls.name)


def home(response):
    return HttpResponse()
