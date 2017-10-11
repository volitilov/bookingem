from django import forms
from .models import Tag


class SearchForm(forms.ModelForm):
	class Meta:
		model = Tag
		fields = "__all__"
	