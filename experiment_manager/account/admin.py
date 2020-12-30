from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Team, TeamUser


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    fields = ('name', 'description')


@admin.register(TeamUser)
class TeamUserAdmin(UserAdmin):

    list_display = ['email', 'username']
