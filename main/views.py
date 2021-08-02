from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

# Create your views here.
def index(response,id):
	ls = ToDoList.objects.get(id=id)
	#item = ls.item_set.get(id=1)
	#return HttpResponse("<h1>%s</h1><br></br><p>%s</p>" %(ls.name,str(item.text)))
	if ls.name:
		return render(response, "main/list.html",{"ls":ls})
	else:
		return render(response, "main/base.html",{})

def v1(response):
	return HttpResponse("v1!</h1>")

def save(response,slug):
	t = ToDoList(name="%s\'s List" %slug)
	t.save()
	return HttpResponse("<h1>%s</h1>" %t.name)

def delete(response,id):
	v = str(id)+"'s List"
	t = ToDoList.objects.filter(name = v)
	t.delete()
	#list = t.objects.all()
	return HttpResponse("<h1>delete %s</h1>" %t.name)

def show(response):
	t = ToDoList.objects.all()
	return HttpResponse("<h1> Table \n%s have</h1>" %t[0])

def home(response):
	return render(response, "main/home.html",{})