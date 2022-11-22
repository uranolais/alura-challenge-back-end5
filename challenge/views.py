from rest_framework import viewsets, generics
from challenge.models import *
from challenge.serializer import *
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class VideoViewSet(viewsets.ModelViewSet):
    '''Exibindo todos os videos'''
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class CategoriaViewSet(viewsets.ModelViewSet):
    '''Exibindo todas as categorias'''
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ListaCategorias(generics.ListAPIView):
    '''Exibindo todos os vídeos de uma categoria específica'''
    def get_queryset(self):
        queryset = Video.objects.filter(categoriaId_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaCategoriaSerializer