from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from models import Question
from django.template import loader
# Create your views here.

def first_page(request):
	question_list = Question.objects.all()
	out = "\n\b,".join([i.question_text for i in question_list])
	template = loader.get_template("blog/index.html")
	context = {"latest_question_list": question_list}
	return render(request, "blog/index.html", context)
	return HttpResponse(template.render(context, request))
	return HttpResponse(out)
	return HttpResponse("<p>my blog</p>")

def detail(request, num):
	question = get_object_or_404(Question, id=num)
	return render(request, "blog/detail.html", {"question":question})
	return HttpResponse(str(num))
