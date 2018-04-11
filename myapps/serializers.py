from rest_framework import serializers
from myapps.models import Users,Blogs

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('fname', 'lanme', 'email','seq','ans')
        #exclude=('seq')

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogs
        fields = '__all__'
        #filels = ('Blog_title', 'Blog_content','email')
        #exclude=('id')



          # This should work :)