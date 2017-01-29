from django.shortcuts import (render, 
							get_object_or_404, render_to_response, redirect)
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.messages import constants as messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
import forms
from models import ActiveSession, QuestionDetail, SubjectCode

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
		try:
			ActiveSession.objects.filter(user = user).delete()
		except:
			pass
		form = forms.FilterForm(request.POST)
		if form.is_valid():
			active = ActiveSession.objects.get_or_create(
				user = user,
				branch = form.cleaned_data['branch'],
				year = form.cleaned_data['year'],
				subject = form.cleaned_data['subject']
				) 
			return HttpResponseRedirect(reverse('select'))
	form = forms.FilterForm()
	return render(request, 'step_1.html', {'user': user, 'form': form})

@login_required(login_url='/login/')
def select(request):

	user = get_object_or_404(User, username = request.user.username)
	active = ActiveSession.objects.get(user=request.user)
	#just find a way to flush out the records of user from ActiveSession once they logout or change fields.
	return render(request, 'home.html', {'user': user, 'active': active})

@login_required(login_url='/login/')
def add_ques(request):
	
	user = get_object_or_404(User, username = request.user.username)
	if request.method=='POST':
		form = forms.QuestionForm(request.POST)
		# print form.errors
		active = get_object_or_404(ActiveSession, user=user)
		print active.subject
		subject = get_object_or_404(SubjectCode, name=active.subject)
		print subject.name
		if form.is_valid():
			question = QuestionDetail.objects.get_or_create(
				owner = user,
				question = form.cleaned_data['question'],
				marks = form.cleaned_data['marks'],
				unit = form.cleaned_data['unit'],
				subject = subject,
				branch = active.branch,
				co = form.cleaned_data['co']
				)
			# messages.success(request, 'Question added!')
			return HttpResponseRedirect('/add_ques/')
	form = forms.QuestionForm()
	return render(request, 'addNew.html', {'user': user, 'form': form})

@login_required(login_url = '/login/')
def view_all(request):
	
	user = get_object_or_404(User, username = request.user.username)
	active = get_object_or_404(ActiveSession, user = user)
	subject = get_object_or_404(SubjectCode, name=active.subject)
	# ques = get_object_or_404(QuestionDetail, subject = subject, branch = active.branch)
	ques = QuestionDetail.objects.filter(subject=subject, branch=active.branch)

	return render(request, 'all_ques.html', {'subject': subject, 'questions': ques})


@login_required(login_url='/login/')
def logout_page(request):
	
	user = get_object_or_404(User, username = request.user.username) 
	try:
		ActiveSession.objects.filter(user = user).delete()
	except:
		pass
	logout(request)
	return HttpResponseRedirect('/')
