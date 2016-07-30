from django import forms
from django.contrib.auth.models import User
from wallpost.models import Category,UserProfile,Post

class UserForm(forms.ModelForm):

	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = ('first_name','last_name','username','email','password')

class CategoryForm(forms.ModelForm):
	
	name = forms.CharField(max_length=128,help_text='Enter the category you want to add')
	slug = forms.CharField(widget=forms.HiddenInput(),required=False)
	class Meta:
		model = Category
		fields = ('name',)

class PostForm(forms.ModelForm):
	
	title = forms.CharField(max_length=128,help_text='Enter the title')
	content = forms.CharField(widget=forms.Textarea)
	class Meta:
		model = Post
		fields = ('title','content','post_image')

class UserProfileForm(forms.ModelForm):
		
		class Meta:
			model = UserProfile
			fields = ('hometown','currrent_city','profession','institution','profile_pic','about_me')
