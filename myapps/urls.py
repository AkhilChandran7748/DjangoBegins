from django.conf.urls import url

from myapps import views

app_name = 'modelforms'










urlpatterns = [

    # /modelforms/
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'logout', views.IndexView.as_view(), name='index'),
    #url(r'^home', views.IndexView.as_view(), name='index'),

    # modelforms/product/entry
    url(r'registration',views.Registration.as_view()),
    url(r'forgot',views.Forgot.as_view()),
    url(r'^newmember', views.register, name='new-user'),
    url(r'^validatelogin',views.login,name='user-exist'),
    url(r'login',views.Login.as_view()),
    url(r'viewblog', views.viewBlog,name='mublogs'),
    url(r'newblog', views.NewBlog.as_view()),
    url(r'^createblog', views.addblog,name='new-blog'),
    url(r'^resetpass', views.resetPassword,name='forgot-password'),
    url(r'reset', views.Reset.as_view()),
    url(r'^user/user_home', views.Backhome.as_view())


]