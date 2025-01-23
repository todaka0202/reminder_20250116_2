from django.shortcuts import render
from django.shortcuts import HttpResponsePermanentRedirect

# from django.shortcuts import HttpResponseRedirect
from django.shortcuts import reverse
from django.views import generic

from .models import Schedule


class IndexView(generic.TemplateView):
    template_name = "reminder/index.html"
    context_object_name = "scedule_title"
    model = Schedule

    def index(self):
        scedule_title = Schedule.objects.order_by("schedule_text")
        context = {"scesule_title": scedule_title}
        return render("reminder/index.html", context)


def SaveSchedule(request):
    c = Schedule(schedule_text=request.POST["text"])

    if c != "":
        c.save()
    return HttpResponsePermanentRedirect(reverse("reminder:index"))
