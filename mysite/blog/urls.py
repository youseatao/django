from django.conf.urls import include, url
import views

urlpatterns = [url(r"^$", views.first_page),
	url(r"^(\d+)$", views.detail, name="detail"),
	url(r"^(\d+)/vote/$", views.vote, name="vote"),
	url(r"^(\d+)/results", views.results)

]
