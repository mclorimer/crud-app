from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

from .forms import EventCreationForm
from .models import Event, Attendance

# Create your views here.
class IndexView(View):
	def get(self, request):
		events = Event.objects.all()
		user = request.user
		context = {
			'events': events,
			'user': user
		}
		return render(request, 'events/index.html', context)


class CreateView(LoginRequiredMixin, View):
	def get(self, request):
		form = EventCreationForm(initial={"creator": request.user})
		return render(request, "events/create.html", {"form":form})

	def post(self, request):
		form = EventCreationForm(request.POST)
		if form.is_valid():
			post = form.save()
			print("form is valid")
			return redirect('/events/index/')
		else:
			return render(request, "events/create.html", {"form":form})

class EditView(LoginRequiredMixin, View):
	def get(self, request, event_id):
		obj = get_object_or_404(Event, id=event_id, creator=request.user)
		form = EventCreationForm(instance=obj)
		context = {
			'form':form
		}

		return render(request, 'events/edit.html', context)


	def post(self, request, event_id):
		obj = get_object_or_404(Event, id=event_id, creator=request.user)

		form = EventCreationForm(request.POST, instance=obj)
		
		if form.is_valid():
			event = form.save()
			return redirect('events:index')
		
		else:
			context = {
				'form': form
			}

			return render(request, 'events/edit.html', context)

class DetailView(LoginRequiredMixin, View):
	def get(self, request, event_id):
		event = Event.objects.get(id=event_id)
		attendees = Attendance.objects.filter(event=event)
		context = {
			"event": event,
			"attendees":attendees
		}
		return render(request, 'events/details.html', context)


class DeleteView(LoginRequiredMixin, View):
	def get(self, request, event_id):
		event = Event.objects.get(id=event_id)
		current_user = request.user
		context = {
			'current_user' : current_user,
			'event' : event
		}

		if request.user != event.creator:
			return render(request, 'events/wrong_user.html', context)
		else:
			return render(request, 'events/delete.html', context)

	def post(self, request, event_id):
		event = Event.objects.get(id=event_id)
		event.delete()
		print('Event deleted!')
		return HttpResponseRedirect('/events/index')


class UserPosts(LoginRequiredMixin, View):
	def get(self, request, username):
		user = User.objects.get(username=username)
		print(user.username)
		pk = user.id
		events = Event.objects.filter(creator=pk)
		events_attending = Attendance.objects.filter(attendee=user)
		context = {
			'user':user,
			'events': events,
			'events_attending': events_attending
		}
		return render(request, "events/user_posts.html", context)


class AttendView(LoginRequiredMixin, View):
	def get(self, request, event_id):
		event = Event.objects.get(id=event_id)

		attendance = Attendance.objects.create(attendee=request.user, event=event)
		print(attendance)

		return render(request, "events/attended.html", {'event':event})