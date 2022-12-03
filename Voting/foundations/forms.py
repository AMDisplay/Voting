from django import forms
from django.contrib.auth.forms import UserCreationForm
from foundations.models import Found, Voting
from foundations.validations import string_validate
from users.models import User


class VotersRegisrationsForm(UserCreationForm):

    voting = forms.ModelChoiceField(queryset=Voting.objects.all())
    foundations = forms.ModelChoiceField(queryset=Found.objects.all())
    id_card = forms.CharField(max_length=8, min_length=8)
    first_name = forms.CharField(validators=[string_validate])
    last_name = forms.CharField(validators=[string_validate])

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('id_card', 'first_name', 'last_name',
                  'voting', 'foundations', 'password1', 'password2')
