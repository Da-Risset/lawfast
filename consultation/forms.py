from django import forms
from .models import Variation

class VariationForm(forms.Form):
    variation_type = forms.ChoiceField(choices=Variation.TYPE_CHOICES, widget=forms.RadioSelect(), required=True)
    variation_duration = forms.ChoiceField(choices=(), widget=forms.RadioSelect(), required=True)

    def __init__(self, consultation_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['variation_duration'].widget.attrs['style'] = 'display: none;'
        self.fields['variation_duration'].choices = Variation.objects.filter(consultation_id=consultation_id).values_list('duration', 'duration')

    def clean(self):
        cleaned_data = super().clean()
        variation_type = cleaned_data.get('variation_type')
        variation_duration = cleaned_data.get('variation_duration')

        if variation_type and variation_duration:
            if Variation.objects.filter(type=variation_type, duration=variation_duration).exists():
                return cleaned_data

        raise forms.ValidationError('Invalid variation selected.')
