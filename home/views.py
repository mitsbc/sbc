from django.http import HttpResponse
from django.shortcuts import render
import datetime
from django.utils import timezone

from home.models import Menu, MenuItem, Widget, SliderItem, CalendarItem, Member, MemberList, Resume
from home.forms import ResumeDropForm

def index(request):
	context = {}
	context['top_menu'] =  Menu.objects.get(name="top")
	context['slider_items'] =  SliderItem.objects.all()
	context['calendar_items'] =  CalendarItem.objects.all().order_by('time').exclude(time__lt=timezone.now())[:3]
	context['left_widget'] =  Widget.objects.get(name="left")
	context['right_widget'] =  Widget.objects.get(name="right")
	return render(request, 'home/index.html', context)

def ine(request):
	context = {}
	context['top_menu'] =  Menu.objects.get(name="top")
	context['today'] = datetime.date.today()
	if request.method == 'POST':
		form = ResumeDropForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			context["submitted"] = True
	else:
		form = ResumeDropForm()
	context["form"] = form
	return render(request, 'home/ine.html', context)

def ine_admin(request):
	context = {}
	context['top_menu'] =  Menu.objects.get(name="top")
	context['today'] = datetime.date.today()
	if request.method == 'POST':
		form = ResumeDropForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			context["submitted"] = True
	else:
		form = ResumeDropForm()
	context["form"] = form
	return render(request, 'home/ine.html', context)

def about(request):
	context = {}
	context['top_menu'] =  Menu.objects.get(name="top")
	return render(request, 'home/about.html', context)

def members_by_name(request, list):
	context = {}
	members = MemberList.objects.get(name=list)
	context['top_menu'] =  Menu.objects.get(name="top")
	context['title'] = members.title
	context['member'] =  members.member.all()
	return render(request, 'home/members.html', context)

def members_by_year(request, year):
	context = {}
	context['top_menu'] =  Menu.objects.get(name="top")
	context['title'] = "Class of %s" % year
	context['member'] =  Member.objects.filter(year=year)
	return render(request, 'home/members.html', context)