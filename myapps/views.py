from django.shortcuts import render
from django.views.generic import TemplateView
from myapps.models import Users,Blogs
from myapps.serializers import UserSerializer,BlogSerializer
from rest_framework import viewsets,generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class AllBlogs(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'user/allblogs.html'
    def get(self, request):
        queryset = Blogs.objects.all()
        serializer_class = BlogSerializer
        return Response({'myblogs':queryset})



class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blogs.objects.all()
    serializer_class =BlogSerializer

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

class IndexView(TemplateView):
    def get(self, request,  **kwargs):
        return render(request,'registration/home.html',context=None)

class Registration(TemplateView):
    template_name = 'registration/registration.html'

class Forgot(TemplateView):
    template_name = 'registration/forgotpass.html'



class Login(TemplateView):
    template_name = 'registration/login.html'
class Myblogs(TemplateView):
    template_name = 'user/viewblog.html'
class NewBlog(TemplateView):
    template_name = 'user/newblog.html'

class Reset(TemplateView):
    template_name = 'user/reset.html'
class Backhome(TemplateView):
    template_name = 'registration/user_home.html'

def register(request):
    if request.method=='POST':
        if request.POST.get('fname') and request.POST.get('lname')  and request.POST.get('email')and request.POST.get('password')and request.POST.get('seq')and request.POST.get('seqans') :
            post = Users()
            post.fname=request.POST.get('fname')
            post.lanme=request.POST.get('lname')
            post.email = request.POST.get('email')
            post.password = request.POST.get('password')
            post.seq = request.POST.get('seq')
            post.ans = request.POST.get('seqans')
            post.save()
            auth_user=User()
            auth_user.first_name=request.POST.get('fname')
            auth_user.last_name=request.POST.get('lname')
            #auth_user.email=
            auth_user.username=request.POST.get('email')
            password=request.POST.get('password')
            auth_user.set_password(password)
            auth_user.is_superuser = 1
            auth_user.save()
            #form=UserCreationForm()
            return render(request, 'registration/home.html')
    else:
            return render(request,'registration/home.html')

def editBlog(request, pk):
    #user = request.session['emailid']
    #print(user)
    l = Blogs.objects.filter(id=pk)
    print(l)
    return render(request, 'user/editblog.html', {'blogs': l})

    #return render(request, template_name="base.html", context={"id": pk})


def login(request):

        email=request.POST.get('email')
        password=request.POST.get('password')
        x=Users.objects.filter(email=email)
        try:
            if x[0].password==password:
                request.session['emailid']=x[0].email
                output = render(request, 'registration/user_home.html')
            else:
                output = render(request, 'registration/login.html')
        except:
            output = render(request, 'registration/login.html')
        return output







def updateblog(request):

            title=request.POST.get('title')
            content=request.POST.get('content')
            blogid=request.POST.get('hid')
            Blogs.objects.filter(id=blogid).update(Blog_title=title,Blog_content=content)
            return render(request, 'registration/user_home.html')






def addblog(request):
    if request.method=='POST':
        if request.POST.get('title') and request.POST.get('content')  :
            post = Blogs();
            post.Blog_title=request.POST.get('title')
            post.Blog_content=request.POST.get('content')
            current_user = request.user
            email=current_user.username
            post.email=email
            post.save()
            return render(request, 'registration/user_home.html')
    else:
        return render(request,'registration/user_home.html')


def viewBlog(request):
    current_user = request.user
    email = current_user.username

    l = Blogs.objects.filter(email=email)
    return render(request, 'user/viewblog.html', {'blogs':l})


def resetPassword(request):
    email = request.POST.get('email')
    seq = request.POST.get('seq')
    ans=request.POST.get('seqans')
    password=request.POST.get('password')
    x = Users.objects.filter(email=email, seq=seq)
    try:
        if x[0].ans == ans:
            Users.objects.filter(email=email).update(password=password)
            output = render(request, 'registration/home.html')
        else:
            output = render(request, 'registration/forgotpass.html')
    except:
        output = render(request, 'registration/forgotpass.html')

    return output



# Create your views here.



# Create your views here.
