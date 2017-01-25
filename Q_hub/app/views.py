from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
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
	form = forms.LoginForm()
	return render(request, 'index.html', {'form': form})

@login_required(login_url='/login/')
def main(request):
	try:
		user = get_object_or_404(User, username=request.user.username)
		return render(request, 'select.html', {'user': user})
	except:
		return HttpResponseRedirect('/')

@login_required(login_url='/login/')
def create_ques(request, username):
	return render_to_response('page_a.html')

@login_required(login_url='/login/')
def logout_page(request):
	logout(request)
	return HttpResponseRedirect('/')
