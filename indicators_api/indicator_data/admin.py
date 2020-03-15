from django.contrib import admin
from django import forms
from django_admin_hstore_widget.forms import HStoreFormField

from .models import DataSet


class DataSetAdminForm(forms.ModelForm):
    data = HStoreFormField()

    class Meta:
        model = DataSet
        exclude = ()


@admin.register(DataSet)
class DataSetAdmin(admin.ModelAdmin):
    form = DataSetAdminForm
    list_display = ('id', 'indicator', 'country', 'num_data',)
    list_filter = ('indicator', 'country',)

    def num_data(self, obj):
        return len(list(filter(None, obj.data.values())))
    num_data.short_description = 'Number of data points'
