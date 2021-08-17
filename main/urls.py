from django.urls import path

from . import views

urlpatterns = [
	path("<int:id>", views.index, name="index"),
	path("v1/", views.v1, name="index"),
	path("save/<slug:slug>", views.save, name="index"),
	path("delete/<int:id>", views.delete, name="index"),
	path("show/", views.show, name="index"),
	path("", views.home, name="home"),
	path("create/",views.create, name="create"),
	path("chi/",views.chi, name="chi"),
]