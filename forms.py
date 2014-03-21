# -*- coding: utf-8 -*-

from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Fieldset, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

from .models import {{ app_name|title }}


class {{ app_name|title }}Form(forms.ModelForm):
    helper = FormHelper()
    helper.layout = Layout(
        Div(
            Submit('save', _(u"Save {{ app_name|title }}"),
                   css_name='btn btn-lg btn-success'),
            HTML('<a href="{% url "{{ app_name }}:list" %}" class="btn '
                 'btn-default">Back</a>'),
            css_name='text-center'
        )
    )

    class Meta:
        model = {{ app_name|title }}
        exclude = ('slug',)
