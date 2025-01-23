from django.shortcuts import render
from django.shortcuts import HttpResponsePermanentRedirect

# from django.shortcuts import HttpResponseRedirect
from django.shortcuts import reverse
from django.views import generic

from .models import Schedule


class IndexView(generic.TemplateView):
    template_name = "reminder/index.html"
    context_object_name = "schedule_title"
    model = Schedule

    def index(self):
        schedule_title = Schedule.objects.order_by("schedule_text")
        context = {"schedule_title": schedule_title}
        return render("reminder/index.html", context)


def SaveSchedule(request):
    c = Schedule(schedule_text=request.POST["text"])

    if c.schedule_text != "":
        c.save()
    return HttpResponsePermanentRedirect(reverse("reminder:index"))
