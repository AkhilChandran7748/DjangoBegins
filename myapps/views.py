from django.shortcuts import render
from django.views.generic import TemplateView
from myapps.models import Users,Blogs
from myapps.serializers import UserSerializer,BlogSerializer
from rest_framework import viewsets


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
            post = Users();
            post.fname=request.POST.get('fname')
            post.lanme=request.POST.get('lname')
            post.email = request.POST.get('email')
            post.password = request.POST.get('password')
            post.seq = request.POST.get('seq')
            post.ans = request.POST.get('seqans')
            post.save()
            return render(request,'registration/login.html')
    else:
            return render(request,'registration/home.html')



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


def addblog(request):
    if request.method=='POST':
        if request.POST.get('title') and request.POST.get('content')  :
            post = Blogs();
            post.Blog_title=request.POST.get('title')
            post.Blog_content=request.POST.get('content')
            post.email=request.session['emailid']
            post.save()
            return render(request, 'registration/user_home.html')
    else:
        return render(request,'registration/user_home.html')


def viewBlog(request):
    user=request.session['emailid']
    print(user)
    l = Blogs.objects.filter(email=user)
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
            output = render(request, 'registration/login.html')
        else:
            output = render(request, 'registration/forgotpass.html')
    except:
        output = render(request, 'registration/forgotpass.html')

    return output



# Create your views here.



# Create your views here.
