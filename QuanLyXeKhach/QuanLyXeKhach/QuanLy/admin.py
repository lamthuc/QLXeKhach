from django.contrib import admin
from .models import Coach
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class AdminCoach(admin.ModelAdmin):
    list_display = []
    search_fields = []
    list_filter =  []

class FormCoach(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)
    class Meta:
        model = Coach
        fields = "__all__"

admin.site.register(Coach, AdminCoach)
# admin.site.register(TuyenXe)
# admin.site.register(NhaXe)
# admin.site.register(VeXe)


