from django.shortcuts import render
from django.http import HttpResponse,  HttpResponseForbidden
import http
import hashlib
import hmac
import json

from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

def index(request, member):
  return HttpResponse('Developer commits be here mon %s' % developer.name)

def detail(request, member):
  return HttpResponse('Developer details will be here %s' % developer.name)

def report(request, member):
  return HttpResponse('Developer reports will be here %s' % developer.name)
