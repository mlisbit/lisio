from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

def resume(request):
    with open(settings.BASE_DIR+'/resume/templates/resume.pdf', 'r') as pdf:
        response = HttpResponse(pdf.read(), mimetype='application/pdf')
        response['Content-Disposition'] = 'inline;filename=resume.pdf'
        return response
    pdf.closed