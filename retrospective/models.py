from django.db import models

from openhumans.models import OpenHumansMember

CERTAINTY_CHOICES = [
    (1, "Random guess"),
    (2, "Very uncertain"),
    (3, "Unsure"),
    (4, "Somewhat certain"),
    (5, "Very certain"),
]


class RetrospectiveEvent(models.Model):
    member = models.ForeignKey(OpenHumansMember, on_delete=models.CASCADE)
    date = models.DateField()
    certainty = models.IntegerField(choices=CERTAINTY_CHOICES)


class RetrospectiveEventAnalysis(models.Model):
    event = models.OneToOneField(RetrospectiveEvent, on_delete=models.CASCADE)
    graph_data = models.TextField()
    graph_image = models.FileField()
