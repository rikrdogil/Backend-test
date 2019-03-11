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

    def validate(self, data):
        
        categoria = data['categoria']
        produto = data['nome']


        for c in categoria:
            produto_data = Produto.objects.filter(categoria__nome__exact = c, nome__exact=produto).values_list('categoria__nome')

        if produto_data:
            raise serializers.ValidationError("Este produto já está cadastrado a categoria escolhida")
        return data


