from django.shortcuts import  get_object_or_404, redirect
from django.views.generic import  TemplateView, CreateView, View
from foundations.models import Found, Voting
from users.models import User
from django.contrib.auth import  login
from foundations.forms import VotersRegisrationsForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render



class Index(TemplateView):
    template_name: str = 'foundations/index.html'


class Seach(View):
    template_name = "foundations/search.html"

    
    def get(self, request):
        query = self.request.GET.get('search', None)
        if query.isdigit():
            user = get_object_or_404(User, id_card = query)
            if user.id_card != user.voting.user.id_card:
                context = {'voter': user}
            else:
                users = user.voting.votings.all()
                context = {'users': users}
        else:
            found = get_object_or_404(Found, name = query)
            voters_for_found = found.found.all()
            context = {'voters_for_found': voters_for_found}
        print(context)
        return render(request, self.template_name, context=context)


class Registrashion(CreateView):
    form_class = VotersRegisrationsForm
    template_name: str = 'registration/register.html'
    success_url = reverse_lazy('index')
    

    def form_valid(self,form):
        user = form.save()
        login(self.request,user)
        return redirect('foundations:index')
