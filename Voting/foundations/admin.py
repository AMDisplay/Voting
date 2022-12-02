from django.contrib import admin
from .models import Voting,Found
from users.models import User

admin.site.register(User)
admin.site.register(Voting)
admin.site.register(Found)
