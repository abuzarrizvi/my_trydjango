from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
	#return HttpResponse("<h1>Hello World</h1>") # string of HTML code
	return render(request,"home.html", {})

def contact_view(request, *args, **kwargs):
	#print(request.user)
	#return HttpResponse("<h1>Contact Page</h1>") # string of HTML code
	return render(request,"contact.html", {})

def about_view(request, *args, **kwargs):
	#return HttpResponse("<h1>About page</h1>") # string of HTML code
	my_context = {
		"title": "abc This is about us",
		"my_number":123,
		"this_is_true":True,
		"my_list": [123,42423,14343, 312, 'ABC'],
		"my_html":"<h1>Hello World</h1>"
	}

	return render(request,"about.html", my_context)

def social_view(request, *args, **kwargs):
	#return HttpResponse("<h1>Social Page</h1>") # string of HTML code
	return render(request,"social.html", {})