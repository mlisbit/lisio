from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render_to_response 
from django.views.generic.base import TemplateView
from django.core.context_processors import csrf
from django.template import RequestContext

from models import Project

# Create your views here.
def home(request):
	args= {}
	args['projects'] = Project.objects.all().extra(order_by = ['priority'])
	args['subtitle'] = 'Projects'
	return render_to_response('projects.html', args, context_instance=RequestContext(request))