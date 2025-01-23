from django.db import models


class Schedule(models.Model):
    schedule_text = models.CharField(max_length=20)

    def __str__(self):
        return self.schedule_text


class DateChoice(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    datechoice_text = models.DateField("date published")

    def __str__(self):
        return self.datechoice_text
