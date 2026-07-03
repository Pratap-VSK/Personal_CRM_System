from django import forms

from .models import Contact, Interaction


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ['user', 'created_at']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control mb-3'})
            if isinstance(field.widget, forms.Select):
                field.widget.attrs['class'] = 'form-select mb-3'


class InteractionForm(forms.ModelForm):
    class Meta:
        model = Interaction
        exclude = ['contact']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control mb-3'})
            if isinstance(field.widget, forms.Select):
                field.widget.attrs['class'] = 'form-select mb-3'
