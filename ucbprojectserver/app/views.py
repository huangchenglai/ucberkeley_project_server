# Create your views here.
from django.shortcuts import *
from django.template import *
from django.http import *


import os,time,datetime,random,sys,math
from itertools import product
from pprint import pprint
import httplib, simplejson, time, datetime
from operator import itemgetter
import MySQLdb
import cPickle
import simplejson


def home(request):
    return render_to_response('home.html')
