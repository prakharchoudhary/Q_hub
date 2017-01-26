from django.shortcuts import (render, 
							get_object_or_404, render_to_response, redirect)
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
import forms	

# Create your views here.
def index(request):

	if request.method=='POST':
		form = forms.LoginForm(request.POST)
		if form.is_valid():
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					return HttpResponseRedirect('/main/')
	form = forms.LoginForm()
	return render(request, 'index.html', {'form': form})

@login_required(login_url='/login/')
def main(request):
	# try:
	# 	user = get_object_or_404(User, username=request.user.username)
	# 	return render(request, 'select.html', {'user': user})
	# except:
	# 	return HttpResponseRedirect('/')

	user = get_object_or_404(User, username = request.user.username)
	if request.method=='POST':
		form = forms.FilterForm(request.POST)
		if form.is_valid():
			details = {
				'branch': form.clean_data['branch'],
				'year': form.clean_data['year'],
				'subject': form.clean_data['subject']
			}
			return redirect('/select/', kwargs={'user':user})
	form = forms.FilterForm()
	return render(request, 'step_1.html', {'user': user, 'form': form})

@login_required(login_url='/login/')
def select(request):
	user = get_object_or_404(User, username = request.user.username)
	return render(request, 'step_2.html', {'user': user})

@login_required(login_url='/login/')
def logout_page(request):
	
	logout(request)
	return HttpResponseRedirect('/')
