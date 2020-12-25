from django.contrib import admin
from .models import Category, Experiment, Tag, Variant, Treatment

# Register your models here.

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    fields = ('name', 'description')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('team', 'type')
    fields = ('team', 'type')


@admin.register(Experiment)
class ExperimentAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_datetime', 'end_datetime')
    fields = ('name', 'start_datetime', 'end_datetime')


@admin.register(Variant)
class VariantAdmin(admin.ModelAdmin):
    list_display = ('name', 'percentage')
    fields = ('name', 'percentage')


@admin.register(Treatment)
class TreatmentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fields = ('name',)
