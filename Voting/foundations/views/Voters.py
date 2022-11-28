from django.shortcuts import render, get_object_or_404
from foundations.models import User
from django.views.generic import DetailView

    
class UsersDetail(DetailView):
    model = User
    template_name: str = "foundations/voters_detail.html"
    

    def get_object(self):
        s = self.request.GET.get("search")
        user = get_object_or_404(self.model, id_card = s)
        return user

    # def get_context_data(self, **kwargs):
    #     search = self.request.GET.get('search')
    #     kwargs['obj'] = get_object_or_404(self.md, id_card = search)

    #     return super().get_context_data(**kwargs)

    # def get_object(self):
    #     search = self.request.GET.get('search')
    #     obj = get_object_or_404(User, id_card = search)
    #     return obj
    # voter = get_object_or_404(User, pk=pk)
    # context = {
    #     'id_card' : voter.id_card,
    #     'name' : voter.first_name,
    #     'surname' : voter.last_name,
    #     'found' : voter.foundations,
    #     'voting' : voter.voting
    # }
    # return render(request, "foundations/voters_detail.html", context)

