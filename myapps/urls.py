from django.conf.urls import url

from myapps import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
app_name = 'modelforms'


urlpatterns = [

    # /modelforms/
    url(r'^login/$', auth_views.login, name='login'),
    #url(r'^login/$',views.my_view, name='login'),
   # url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'logout', views.logout_view, name='logout'),
    #url(r'^home', views.IndexView.as_view(), name='index'),
    url(r'^user/ajax', TemplateView.as_view(template_name='user/ajax.html')),
    # modelforms/product/entry
    url(r'registration',views.Registration.as_view()),
    url(r'forgot',views.Forgot.as_view()),
    url(r'^newmember', views.register, name='new-user'),
    url(r'^validatelogin',views.login,name='user-exist'),
    # url(r'login',views.Login.as_view()),
    url(r'viewblog', views.viewBlog,name='mublogs'),
    url(r'newblog', views.NewBlog.as_view()),
    url(r'^createblog', views.addblog,name='new-blog'),
    url(r'^updateblog', views.updateblog,name='new-blog'),
    url(r'^resetpass', views.resetPassword,name='forgot-password'),
    url(r'allblogs', views.AllBlogs.as_view(), name='all blogs'),
    url(r'reset', views.Reset.as_view()),
    url(r'^user/user_home', views.Backhome.as_view()),

    url(r'^user/blogid=(?P<pk>[0-9]+)$', views.editBlog, name='index'),


    url(r'^password/$', views.change_password, name='change_password'),
    url(r'^user/likeid=(?P<pk>[0-9]+)$', views.addLike, name='likes')
    #url(r'images/like',views.like.as_view())


]