from rest_framework import serializers
from . import models



class NaturezaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__' 
        model = models.NaturezaDespesas
        

class FornecedoresSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__' 
        model = models.Fornecedores
        
        
        
class NotasFiscaisSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__' 
        model = models.NotasFiscais
        
        
class ItensNotaFiscalSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__' 
        model = models.ItensNotaFiscal
        
class EstadosBemSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__' 
        model = models.EstadosBem
        
        
class SituacaoUsoBemSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__' 
        model = models.SituacaoUsoBem
        
        
class MarcasSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__' 
        model = models.Marcas
        
        
class BensSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__' 
        model = models.Bens

        
        

