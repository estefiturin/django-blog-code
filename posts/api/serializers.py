from rest_framework.serializers import ModelSerializer
from posts.models import Post

class PostSerializer(ModelSerializer):
    class Meta: 
        model = Post #le pasamos el modelo post
        fields = ['title', 'description', 'order', 'created_at'] #usamos estos campos 
        # fields = '__all__'
    