from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render_to_response 
from django.views.generic.base import TemplateView
from django.core.context_processors import csrf
from django.template import RequestContext
from django.conf import settings
from models import Statement

def home(request):
	args= {}
	try:
		args['statement'] = Statement.objects.all()[0]
	except:
		pass
	return render_to_response('index.html', args, context_instance=RequestContext(request))

def resume(request):
    with open(settings.BASE_DIR+'/lisio/templates/resume.pdf', 'r') as pdf:
        response = HttpResponse(pdf.read(), mimetype='application/pdf')
        response['Content-Disposition'] = 'inline;filename=resume.pdf'
        return response
    pdf.closed