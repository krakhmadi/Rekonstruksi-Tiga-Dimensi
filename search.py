from django import forms
from .models import Post

class SearchName(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('longitude', 'latitude')

        widgets = {
            'longitude': forms.NumberInput(attrs={'class': 'form-control'}),
            'latitude': forms.NumberInput(attrs={'class': 'form-control'}),
            # 'image': forms.FileInput(attrs={'class': 'form-control'}),
            # 'texture_map': forms.FileInput(attrs={'class': 'form-control'}),
        }
