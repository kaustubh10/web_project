from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from wallpost.models import Category,Post,UserProfile
from wallpost.forms import UserForm,CategoryForm,PostForm,UserProfileForm
from django.contrib.auth import authenticate,login,logout

def index(request):
	
	if request.user.is_authenticated():	
		user = get_object_or_404(User,username=request.user.username)
		category = Category.objects.all()
	
		context = {
			'user':user,
			'category':category,
			}
	else:
		context={}
	return render(request,'index.html',context)

def user_login(request):
	
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		
		user = authenticate(username=username,password=password)
		if user:
			if user.is_active:
				login(request,user)
				return HttpResponseRedirect('/wallpost/')
			else:
				return HttpResponse('Your session is dropped')
		else:
			return HttpResponse('Invalid username/password')
	else:
		return render(request,'login.html',{})

def signup(request):

	registered = False
	if request.method == "POST":
		
		form = UserForm(request.POST or None)
		if form.is_valid():
			
			user = form.save()
			user.set_password(user.password)
			user.save()
			registered = True
		else:
			print form.errors
	else:
		form = UserForm()
	return render(request,'signup.html',{'form':form,'registered':registered})


def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/wallpost/')

def category(request,category_slug):
		
	category = get_object_or_404(Category,slug=category_slug)
	post = Post.objects.filter(category=category)
	return render(request,'category.html',{'category':category,'post':post})

def add_category(request):
		
	instance = get_object_or_404(User,username=request.user)
	a = Category(category_user=instance)
	if request.method == "POST":
		form = CategoryForm(request.POST or None,instance=a)
		if form.is_valid():
			cat = form.save(commit=False)
			cat.save()
			return HttpResponseRedirect('/wallpost/')
		else:
			print form.errors
	else:
		form = CategoryForm()
	return render(request,'add_category.html',{'form':form})

def create_post(request,category_slug):
	
	instance = get_object_or_404(Category,slug=category_slug)
	user = get_object_or_404(User,username=request.user)
	a = Post(category=instance,post_user=user)
	if request.method == "POST":
		form = PostForm(request.POST,request.FILES,instance=a)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			return category(request,category_slug)
		else:
			print form.errors
	else:
		form = PostForm()
	return render(request,'create_post.html',{'form':form,'instance':instance})

def post(request,category_slug,id=id):
	
	instance = get_object_or_404(Post,id=id)
	return render(request,'post.html',{'instance':instance})

def update_profile(request):
	
	if request.user.is_authenticated():
		instance = get_object_or_404(UserProfile,user=request.user)
		if request.method == "POST":

			form = UserProfileForm(request.POST,request.FILES,instance=instance)
			if form.is_valid():
				userprofile = form.save(commit=False)
				userprofile.save()
				return HttpResponseRedirect('/wallpost/')
			else:
				print form.errors
		else:
			form = UserProfileForm()
	
	return render(request,'update_profile.html',{'form':form,'instance':instance})

def profile(request):
	
	if request.user.is_authenticated():
		userprofile = get_object_or_404(UserProfile,user=request.user)
		posts = Post.objects.filter(post_user=request.user)
		categories = Category.objects.filter(category_user=request.user)
		context = {
			'userprofile':userprofile,
			'posts':posts,
			'categories':categories,
			}
	else:
		context = {}

	return render(request,'profile.html',context)
