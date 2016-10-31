from django.shortcuts import render

import logging
import time

from .models import Talk

log = logging.getLogger(__name__)

def index(request):
    import web_pdb
    web_pdb.set_trace()
    log.info("Hello Pycon")
    talks = Talk.objects.all().select_related()
    log.info("Rendering")
    return render(request, 'webpdbexample/index.html',
        {'year':2016, "talks":talks})

def on_exception(request):
    log.info("Hello Pycon")
    talks = Talk.objects.all().select_related()
    import web_pdb
    with web_pdb.catch_post_mortem():
        raise Exception("Whoops")
    log.info("Rendering")
    return render(request, 'webpdbexample/index.html',
        {'year':2016, "talks":talks})

