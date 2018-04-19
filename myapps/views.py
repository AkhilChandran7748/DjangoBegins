from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from myapps.models import Users,Blogs,Like,Comment
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
        curuser = request.user
        uid=curuser.id
        queryset = Blogs.objects.all()
        serializer_class = BlogSerializer
        count=0
        c=[]
        lc=[]
        for i in queryset:
            q = Like.objects.filter(bid=i.id)
            r = Like.objects.filter(bid=i.id,uid=uid)
            #print(r.count)
            if r.count()==0:
                lc.append(True)
            else:
                lc.append(False)
            #lc.append(r.count())
            c.append(q.count())
        d=zip(queryset, c,lc)
        return Response({'myblogs':queryset,'c':c,'d':d})



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


def viewMore(request,pk):
    blog = Blogs.objects.get(id=pk)
    comments=Comment.objects.filter(bid=blog.id)
    l=comments.count()
    u=[]
    for i in range(0,l):
        uname=comments[i].uid
        u.append(uname.username)
    print(u)
    d = zip(comments, u)
    return render(request, 'user/viewmore.html', {'blog': blog,'cmt':d})


def addLike(request,pk):
    like=Like()
    like.bid=pk
    curuser=request.user

    like.uid=curuser
    like.save()

    queryset = Blogs.objects.all()
    c = [] # likes for a blog
    lc = [] #like count for a user
    for i in queryset:
        q = Like.objects.filter(bid=i.id)
        r = Like.objects.filter(bid=i.id, uid=curuser.id)
        # print(r.count)
        if r.count() == 0:
            lc.append(True)
        else:
            lc.append(False)
        # lc.append(r.count())
        c.append(q.count())
    d = zip(queryset, c, lc)
    return  render(request,'user/allblogs.html',{ 'd': d})


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

@csrf_exempt
def addcomment(request):

            comment= request.POST.get('comment')
            curuser = request.user
            uid = curuser
            bid=request.POST.get('hid')
            cmt=Comment()
            cmt.uid=uid
            cmt.bid=bid
            cmt.comment=comment
            cmt.save()
            print("ID:",bid)
            queryset = Blogs.objects.all()
            c = []
            lc = []
            for i in queryset:
                q = Like.objects.filter(bid=i.id)
                r = Like.objects.filter(bid=i.id, uid=curuser.id)
                # print(r.count)
                if r.count() == 0:
                    lc.append(True)
                else:
                    lc.append(False)
                # lc.append(r.count())
                c.append(q.count())
            d = zip(queryset, c, lc)
            return render(request, 'user/allblogs.html', {'d': d})

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


from django.contrib.auth import logout

def logout_view(request):
    logout(request)
   # django.contrib.auth.logout()
    return render(request, 'registration/home.html')
# Create your views here.



# Create your views here.

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'user/change_password.html', {
        'form': form
    })