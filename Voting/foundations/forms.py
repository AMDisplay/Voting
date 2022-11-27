from django import forms
from django.contrib.auth.forms import UserCreationForm
from foundations.models import Voting, Foundations, User
from django.core.validators import MinValueValidator


class VotersRegisrationsForm(UserCreationForm):
    voting = forms.ModelChoiceField(queryset=Voting.objects.all())
    foundations = forms.ModelChoiceField(queryset=Foundations.objects.all())
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('id_card','first_name', 'last_name', 'voting', 'foundations', 'password1', 'password2')


