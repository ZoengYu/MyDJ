from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .form import CreateNewList

# Create your views here.
def index(response,id):
	ls = ToDoList.objects.get(id=id)
	#item = ls.item_set.get(id=1)
	#return HttpResponse("<h1>%s</h1><br></br><p>%s</p>" %(ls.name,str(item.text)))

	if response.method == "POST":
		print(response.POST)
		if response.POST.get("save"):
			for item in ls.item_set.all():
				if response.POST.get("c"+str(item.id)) == "on":
					item.complete = True
				else:
					item.complete = False
				
				item.save()
		elif response.POST.get("newItem"):
			txt = response.POST.get("new")
			if len(txt) > 2:
				ls.item_set.create(text=txt, complete=False)
			else:
				print("invalid")
		elif response.POST.get("delete"):
			for item in ls.item_set.all():
				print(item.id)
				if response.POST.get("c"+str(item.id)) == "on":
					delete_ID = item.id
					print(ls.item_set.filter(id=delete_ID))
					ls.item_set.filter(id=delete_ID).delete()

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
	if response.method == "POST":
		print(response.POST)
		if response.POST.get("delete"):
			for item in t:
				if response.POST.get("c"+str(item.id)) == "on":
					print("delete table: ")
					t.filter(id=item.id).delete()
			return HttpResponseRedirect("/show/")
		elif response.POST.get("new"):
			txt = response.POST.get("new")
			if len(txt)<1:
				return render(response, "main/show.html",{"t":t})
			else:
				t.create(name=txt)
				
	return render(response, "main/show.html",{"t":t})

def home(response):
	return render(response, "main/home.html",{})

def create(response):
	if response.method == "POST": #POST will encrypt
	  form = CreateNewList(response.POST) #create dictionary and save value into
	  if form.is_valid(): #check all value have input
	    	n = form.cleaned_data["name"] #get name by user type
	    	t = ToDoList(name=n)
	    	t.save()
	  return HttpResponseRedirect("/%i" %t.id)
	else: #GET
		form = CreateNewList()
	return render(response,"main/create.html", {"form":form})