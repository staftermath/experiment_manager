from django.contrib import admin
from .models import Category, Experiment, Tag, Variant, Treatment


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
    list_display = ('name', 'start_datetime', 'end_datetime', 'category')
    fields = (
        'name',
        'start_datetime',
        'end_datetime',
        'category',
        'variants',
        'description',
        'doc',
        'config'
    )


@admin.register(Variant)
class VariantAdmin(admin.ModelAdmin):
    list_display = ('name', 'percentage')
    fields = ('name', 'percentage', 'treatments')


@admin.register(Treatment)
class TreatmentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fields = ('name', 'tags')
