from rest_framework import serializers

from .models import Produto, Categoria

class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = ('id', 'nome')

        

class ProdutoSerializer(serializers.ModelSerializer):

    categoria = CategoriaSerializer(read_only=True, many=True)
    categoria_id = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all(), write_only=True, source='categoria', many=True)

    class Meta:
        model = Produto
        fields = ('id','nome', 'preco','categoria', 'categoria_id')
