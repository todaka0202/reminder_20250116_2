# from django.shortcuts import render
from django.shortcuts import HttpResponsePermanentRedirect

# from django.shortcuts import HttpResponseRedirect
from django.shortcuts import reverse
from django.views import generic
# from datetime import datetime

from .models import Task


class IndexView(generic.TemplateView):
    template_name = "reminder/index.html"
    context_object_name = "title"
    model = Task

    def get_queryset(self):
        return Task.objects.order_by("reminder_time")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.get_queryset()
        return context


def SaveSchedule(request):
    if request.POST:
        title = request.POST.get("title")
        reminder_time = request.POST.get("reminder_time")

        schedule = Task(title=title, reminder_time=reminder_time)

        if schedule != "":
            if reminder_time != "":
                schedule.save()
            else:
                return HttpResponsePermanentRedirect(reverse("reminder:index"))
    return HttpResponsePermanentRedirect(reverse("reminder:index"))
