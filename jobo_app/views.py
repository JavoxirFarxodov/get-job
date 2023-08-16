from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView
from . import models


# Create your views here.


# class IndexView(TemplateView):
#     template_name = 'index.html'
@login_required(login_url='/users/register')
def IndexView(request):
        return render(request, 'jobo/index.html')


@login_required(login_url='/users/register')
def AboutView(request):
    return render(request, 'jobo/about.html')


@login_required(login_url='/users/register')
def CategoriesView(request, type_category):
    jobs = models.JobModel.objects.filter(category_id=type_category)
    print(jobs)
    return render(request, 'jobo/category.html',
                  context={
                      'jobs': jobs
                  })


@login_required(login_url='/users/register')
def user_profile(request):
    return render(request, 'jobo/user_profile.html', {'user': request.user})


@login_required(login_url='/users/register')
def contact(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']
        from_email = request.POST['from_email']
        send_mail(subject, message, from_email, ['your_email@example.com'])
        return HttpResponseRedirect(reverse('contact'))

    return render(request, 'jobo/contact.html')


@login_required(login_url='/users/register')
def search_view(request):
    search_query = request.GET.get('search')
    if search_query is not None:
        results = models.JobModel.objects.filter(title__icontains=search_query)
    else:
        results = 'None'
    return render(request, 'jobo/search.html', context={'data': results})


def fulltime(request):
    jobs = models.JobModel.objects.all()
    return render(request, "jobs.html", context={"jobs": jobs})
