from rest_framework import viewsets

from .serializers import ProdutoSerializer, CategoriaSerializer
from .models import Produto, Categoria



class CategoriaViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriaSerializer
    queryset = Categoria.objects.all()


class ProdutoViewSet(viewsets.ModelViewSet):
        serializer_class = ProdutoSerializer
        queryset = Produto.objects.all()
