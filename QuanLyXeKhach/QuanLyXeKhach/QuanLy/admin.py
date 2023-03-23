from django.contrib import admin
from .models import ChuyenXe, TuyenXe, NhaXe, VeXe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class AdminChuyenXe(admin.ModelAdmin):
    list_display = ['tuyenxe', 'nhaxe', 'gio_den', 'gio_di']
    search_fields = ['tuyenxe', 'nhaxe']
    list_filter =  ['tuyenxe', 'nhaxe']

class FormChuyenXe(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)
    class Meta:
        model = ChuyenXe
        fields = "__all__"

admin.site.register(ChuyenXe, AdminChuyenXe)
admin.site.register(TuyenXe)
admin.site.register(NhaXe)
admin.site.register(VeXe)


