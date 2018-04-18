from django.db import models

class Users(models.Model):
    fname = models.CharField(max_length=40)
    lanme = models.CharField(max_length=40)
    email = models.CharField(max_length=40, unique=True)
    password=models.CharField(max_length=40)
    seq=models.CharField(max_length=40)
    ans=models.CharField(max_length=40)

    def __str__(self):
        return self.fname + " " + self.lanme

class Blogs(models.Model):
      Blog_title = models.CharField(max_length=40)
      Blog_content = models.CharField(max_length=150)
      email=models.CharField(max_length=40)
      #email = models.ForeignKey(Users,db_column='email')


      def __str__(self):
        return self.Blog_title

# Create your models here.
class Like(models.Model):
    uid=models.ForeignKey('auth.User', on_delete=models.CASCADE)
    bid = models.IntegerField()



