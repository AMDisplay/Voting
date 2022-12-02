from django import forms
from django.contrib.auth.forms import UserCreationForm
from foundations.models import Voting, Found
from users.models import User


class VotersRegisrationsForm(UserCreationForm):
    voting = forms.ModelChoiceField(queryset=Voting.objects.all())
    foundations = forms.ModelChoiceField(queryset=Found.objects.all())
    id_card = forms.IntegerField(min_value=8, max_value=8)
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('id_card','first_name', 'last_name', 'voting', 'foundations', 'password1', 'password2')


