from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from posts.models import Post
from posts.api.serializers import PostSerializer
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
#agrego mi propio permiso
from posts.api.permissions import IsAdminOrReadOnly

#CRUD, devuelve el CRUD completo
class PostModelViewSet(ModelViewSet):
    #dar permiso para que solo autentificados puedan realizar cambios
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = PostSerializer
    queryset= Post.objects.all()

'''
class PostViewSet(ViewSet):
    def list(self, request):
        serializer = PostSerializer(Post.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    #obtener datos de un solo post, obtiene mediante su ID(pk)
    def retrieve(self,request, pk: int):
        post = PostSerializer(Post.objects.get(pk=pk))
        return Response(status=status.HTTP_200_OK, data=post.data)
       
    def create(self,request):
        serializer = PostSerializer(data=request.POST)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK, data=serializer.data)    
'''

'''
#necesario generar un serializador
class PostApiView(APIView):
    def get(self, request):#obtener endpoints
        #posts = Post.objects.all() #todos los elementos de la BD
        #posts = [post.title for post in Post.objects.all()] 
        serializer = PostSerializer(Post.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    def post(self, request):
        #ejecutamos serializador y pasamos datos
        serializer = PostSerializer(data=request.POST)
        #validar datos
        serializer.is_valid(raise_exception=True)
        #guardar dato en la base de datos
        serializer.save()
        return Response(status=status.HTTP_200_OK, data=serializer.data)
'''

