from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
	title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder":"Your Title"}))
	email = forms.EmailField()
	description = forms.CharField(
		required=False, 
		widget=forms.Textarea(
			attrs={
				"class":"new-class-name two",
				"rows": 20,
				"placeholder":"Your description",
				"id":"my-id-for-textarea",
				"cols" :120
			}
			)
		)
	price = forms.DecimalField(initial=199.00)

	class Meta:
		model = Product
		fields = [
		 	'title',
		 	'description',
		 	'price'
		]
	def clean_title(self,*args, **kwargs):
		title = self.cleaned_data.get("title")
		if not "abuzar" in title:
			raise forms.ValidationError("This is not a valid title")
		if not "news" in title:
			raise forms.ValidationError("This is not a valid title")
		return title

	def clean_email(self,*args, **kwargs):
		email = self.cleaned_data.get("email")
		if not email.endswith("edu"):
			raise forms.ValidationError("This is not a valid email")
		
		return title
		
			

class RawProductForm(forms.Form):
	title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder":"Your Title"}))
	description = forms.CharField(
		required=False, 
		widget=forms.Textarea(
			attrs={
				"class":"new-class-name two",
				"rows": 20,
				"placeholder":"Your description",
				"id":"my-id-for-textarea",
				"cols" :120
			}
			)
		)
	price = forms.DecimalField(initial=199.00)