# Create your views here.
from django.template import RequestContext
from django.shortcuts import *
from django.core.cache import cache
from django.contrib import auth
from django.contrib.auth import *
from django.contrib.auth.forms import *
from django.contrib.auth.models import *
from django.views.decorators.http import condition, etag, last_modified
from django.utils.http import urlencode
from django.template import *
from django.core.mail import EmailMessage
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.http import HttpResponse


import time, datetime,random,sys, math
from itertools import product
from pprint import pprint
import httplib, simplejson, time, datetime
from operator import itemgetter
import MySQLdb
import cPickle
import simplejson


def home(request):
    html = "<html><body><h2>You are viewing the Home Page</h2>It is now %s.</body></html>" % datetime.datetime.now()
    #return HttpResponse(html)
    return render_to_response('/templates/home.html')
    #not sure why this isn't working