from django.shortcuts import render_to_response
from django.template import RequestContext
from main.models import Student

def index(request):
	return render_to_response('index.html', {
	         }, RequestContext(request))

def hijo(request):
	return render_to_response('hijo.html', {
         }, RequestContext(request))

def include(request):
	return render_to_response('include.html', {
         }, RequestContext(request))


def loop(request):
	students = Student.objects.all()	
	return render_to_response('loop.html', {
	"students" : students
         })

