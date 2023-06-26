from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            # 'longitude': forms.TextInput(attrs={'class': 'form-control'}),
            # 'latitude': forms.TextInput(attrs={'class': 'form-control'}),
            # 'image': forms.FileInput(attrs={'class': 'form-control'}),
            # 'texture_map': forms.FileInput(attrs={'class': 'form-control'}),
        }


