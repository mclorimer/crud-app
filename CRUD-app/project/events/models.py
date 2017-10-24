from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Event(models.Model):
	title = models.CharField(max_length=40)
	content = models.TextField()
	created_at = models.DateTimeField(default=timezone.now)
	date = models.DateTimeField()
	creator = models.ForeignKey(User)
	location = models.CharField(max_length=100)
	attendees = models.ManyToManyField(
		User, through='events.Attendance',
		through_fields=('event', 'attendee'),
		related_name='attendees'
		)

	def __str__(self):
		return self.title


class Attendance(models.Model):
	attendee = models.ForeignKey(User)
	event = models.ForeignKey(Event)

	def __str__(self):
		return "{}".format(self.event)