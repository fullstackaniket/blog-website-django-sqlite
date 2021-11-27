from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from .models import Cate,BlogInfo,Profile,BascicSettings,Profile
from .forms import BlogPostForms,CategoryPostForms,SignUpForm,PostEditForm
from django.contrib.auth import login as auth_login,logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.db.models import Q


# Create your views here.

def index(request):

  cat = Cate.objects.filter(c_status = "show")
  bloginfo=BlogInfo.objects.all()
  basic=BascicSettings.objects.all()
  query=request.GET.get('s')
  if query:
      bloginfo = BlogInfo.objects.filter(
          Q(title__icontains=query)|
          Q(body__icontains=query)|
          Q(author__username=query)
          )
  
  data = {
      'cat':cat,
      'bloginfo':bloginfo,
      'basic':basic,
      

  }
  return render(request,"index.html",data)
def category(request):
    return render(request,"category.html")
def contact(request):
    data=BascicSettings.objects.all()
    return render(request,"contact.html",{'data':data})
def styles(request):
    return render(request,"styles.html")
def about(request):
    data=BlogInfo.objects.all()

    return render(request,"about.html",{'data':data})
def singleaudio(request):
    return render(request,"singleaudio.html")

def singlevideo(request):
    
    return render(request,"singlevideo.html")

def post_edit(request,id):
    post=get_object_or_404(BlogInfo,id=id)
    if request.method == "POST":
        form=PostEditForm(request.POST or None,instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(post.get_absolute_url())
    else:
        form = PostEditForm(instance=post)
    data ={
        'post':post,
        "form":form,
    }
    return render(request,"post.html",data)

def like_post(request):
    s_blog = get_object_or_404(BlogInfo, id = request.POST.get('id'))
    is_liked = False
    if s_blog.likes.filter(id = request.user.id).exists():
        s_blog.likes.remove(request.user)
        is_liked = False
    else:
        s_blog.likes.add(request.user)
        is_liked = True
    data = {
        'blog':s_blog,
        'is_liked' : is_liked,
        'total_likes': s_blog.total_likes(),

    }
    if request.is_ajax():
        html = render_to_string("like.html", data, request = request)
        return JsonResponse({'form':html})

def singlestandard(request,id,slug):
    s_blog = get_object_or_404(BlogInfo,id = id)
    is_liked = False
    if s_blog.likes.filter(id =request.user.id).exists():
        is_liked = True
    data ={
        'blog':s_blog,
        'is_liked':is_liked,
        'total_likes':s_blog.total_likes(),
        }
        
   # print(data)
    return render(request,"singlestandard.html",data)


def basic(request):
    
   # if request.GET:
        #a= request.POST["fname"]  this is for accessing values of form  her fname and lname is name to the input field  in the form
        #b= request.POST["lname"]
   #    print(request.GET)  #it prints all data of form  
    c=Cate()  # creating object for class Cate
    
    if request.POST:  # when using post method u have to create a token
        a= request.POST["fname"]  # fname and lname are names of input fields in the form
        b= request.FILES["lname"]  # use request.FILES method for getting data of type File of image
       # c= request.POST["aaaa"]
        c.c_name = a 
          # inserting value of "a" in c_name of Cate
        c.c_img = b 
            # inserting value of "b" in c_img of Cate 
        c.c_status = c
        c.save()    # it saves the data to table and then object is destroyed
        print(request.POST)
        print(a)
        print(b)
        #print(c)
       
    return render(request,"basic.html")


def blogpost(request):
    if request.method == "POST":
        form = BlogPostForms(request.POST,request.FILES)
        print(form.is_valid())
        if form.is_valid():
            print("hello")
            post = form.save(commit= False)
            post.author = request.user
            post.save()
            return redirect("index")
    else:
        form= BlogPostForms()
    data = { 
        
        'form':form,
    }
    return  render(request,'blogpost.html', data)

def signup(request):
    if request.method == 'POST':
        form=SignUpForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            user=form.save()
            user.refresh_from_db()
            user.profile.dob=form.cleaned_data.get('dob')
            user.save()
            raw_password=form.cleaned_data.get('password')
            user=authenticate(username=user.username,password=raw_password)
            auth_login(request,user)
            return redirect('index')
    else:
        form=UserCreationForm()
    return render (request,"signup.html",{'form':form})


def login(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() 
            auth_login(request,user)
            return redirect('index')
    else:
        form=UserCreationForm()
    return render(request,"login.html",{'form':form})

def logout(request):
    auth_logout(request)
    return redirect('index')

 

def signup1(request):
    if request.method == 'POST':
        form=SignUpForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            user=form.save()
            user.refresh_from_db()
            user.profile.dob=form.cleaned_data.get('dob')
            user.save()
            raw_password=form.cleaned_data.get('password1')
            user=authenticate(username=user.username,password=raw_password)
            auth_login(request,user)
            return redirect('index')
    else:
        form=SignUpForm()

    return render(request,"signup1.html",{'form':form})



def display(request):
    if request.user.is_authenticated:
        # user=Profile.objects.get(user=request.user)
        cat = Cate.objects.filter(c_status = "show")
        bloginfo=BlogInfo.objects.filter(author=request.user)
       

        data = {
            'cat':cat,
            'bloginfo':bloginfo,
           
            #'user':user,
              }
    
        print(bloginfo)
    return render(request,"display.html",data)

def base(request):
    cat = Cate.objects.filter(c_status = "show")
    bloginfo=BlogInfo.objects.all()
    basic=BascicSettings.objects.all()
  
    data = {
      'cat':cat,
      'bloginfo':bloginfo,
      'basic':basic,
       }

    return render(request, "base.html",data)


def cate_edit(request):
            

    return render(request, "index")
