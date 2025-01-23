# from django.shortcuts import render
from django.shortcuts import HttpResponsePermanentRedirect

# from django.shortcuts import HttpResponseRedirect
from django.shortcuts import reverse
from django.views import generic

from .models import Schedule


class IndexView(generic.TemplateView):
    template_name = "reminder/index.html"


def SaveSchedule(request):
    c = Schedule(event_text=request.POST["text"])

    if c != "":
        c.save()
    return HttpResponsePermanentRedirect(reverse("reminder:index"))
