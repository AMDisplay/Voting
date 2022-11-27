from django.contrib import admin
from .models import Voting,Foundations,User

admin.site.register(User)
admin.site.register(Voting)
admin.site.register(Foundations)
