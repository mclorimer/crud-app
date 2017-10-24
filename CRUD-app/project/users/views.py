from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

from passlib.hash import pbkdf2_sha256
from .forms import SignUpForm

class SignUp(View):
	
	def post(self, request):
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return HttpResponseRedirect('/events/index/')
	
	def get(self, request):
		form = SignUpForm()
		return render(request, 'users/signup.html', {'form': form})


class DeleteUser(View):
	def get(self, request, username):
		user = User.objects.get(username=username)
		return render(request, 'users/delete.html', {'user':user})

	def post(self, request, username):

		user = User.objects.get(username=username)
		logout(request)
		user.delete()
		print("user deleted!")
		return HttpResponseRedirect('/events/index')

class LogoutView(View):
	def get(self, request):
		logout(request)
		return HttpResponseRedirect('/')