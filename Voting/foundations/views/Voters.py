from django.shortcuts import render, get_object_or_404, redirect
from foundations.models import User


    
def UsersDetail(request,pk):
    voter = get_object_or_404(User, pk=pk)
    context = {
        'id_card' : voter.id_card,
        'name' : voter.first_name,
        'surname' : voter.last_name,
        'found' : voter.foundations,
        'voting' : voter.voting
    }
    return render(request, "foundations/voters_detail.html", context)

