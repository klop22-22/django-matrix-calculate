from django.contrib import admin

from users.models import User, UserHistory

admin.site.register(User)

admin.site.register(UserHistory)