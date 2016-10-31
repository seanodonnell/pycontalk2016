from django.shortcuts import render

import logging
import time

from .models import Talk

log = logging.getLogger(__name__)

def index(request):
    log.info("Hello Pycon")
    #talks = Talk.objects.all()
    talks = Talk.objects.all().select_related()
    log.info("Rendering")
    return render(request, 'debugtoolbarexample/index.html',
        {'year':2016, "talks":talks})
