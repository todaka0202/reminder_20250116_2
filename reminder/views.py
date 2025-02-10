from django.shortcuts import render
from django.shortcuts import HttpResponsePermanentRedirect

# from django.shortcuts import HttpResponseRedirect
from django.shortcuts import reverse
from django.views import generic
from datetime import datetime

from .models import Task


class IndexView(generic.TemplateView):
    template_name = "reminder/index.html"
    context_object_name = "title"
    model = Task

    def get_queryset(self):
        return Task.objects.order_by("title")

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
            schedule.save()

    return HttpResponsePermanentRedirect(reverse("reminder:index"))


def list(request):
    # 今日の分のみの絞り込みチェックボックス
    only_today = request.GET.get("only_today")
    if only_today is not None:
        # 今日の日付の分のみ（reminder_timeは時分秒以下も持っているので日付までで比較）
        tasks = Task.objects.filter(reminder_time__date=datetime.now().date())
        context = {"tasks": tasks}
    else:
        tasks = Task.objects.all()
    return render(request, "reminder/index.html", context)
