from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import View
from django.views.generic import ListView, TemplateView, DetailView,CreateView
from foundations.models import Foundations, User
from django.contrib.auth import authenticate, login
from foundations.forms import VotersRegisrationsForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404


class Index(TemplateView):
    template_name: str = 'foundations/index.html'
    


class Registrashion(CreateView):
    form_class = VotersRegisrationsForm
    template_name: str = 'registration/register.html'
    success_url = reverse_lazy('index')
    

    def form_valid(self,form):
        user = form.save()
        login(self.request,user)
        return redirect('foundations:index')


def FoundDetail(request,pk):
    found = get_object_or_404(Foundations, pk=pk)
    voting = found.found_voting.all()
    voters = found.found_voters.all()
    context = {
        'name' : found.name,
        'voters' : voters,
        'voting' : voting
    }
    return render(request, "foundations/found_detail.html", context)