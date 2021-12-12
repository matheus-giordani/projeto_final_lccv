from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers

# Create your views here.

class NaturezaDespesasView(viewsets.ModelViewSet):
    queryset = models.NaturezaDespesas.objects.all()
    serializer_class = serializers.NaturezaSerializer
    
class FornecedoresView(viewsets.ModelViewSet):
    queryset = models.Fornecedores.objects.all()
    serializer_class = serializers.FornecedoresSerializer
    
class NotasFiscaisView(viewsets.ModelViewSet):
    queryset = models.NotasFiscais.objects.all()
    serializer_class = serializers.NotasFiscaisSerializer
    
class ItensNotaFiscalView(viewsets.ModelViewSet):
    queryset = models.ItensNotaFiscal.objects.all()
    serializer_class = serializers.ItensNotaFiscalSerializer
    
class EstadosBemView(viewsets.ModelViewSet):
    queryset = models.EstadosBem.objects.all()
    serializer_class = serializers.EstadosBemSerializer
    
class SituacaoUsoBemView(viewsets.ModelViewSet):
    queryset = models.SituacaoUsoBem.objects.all()
    serializer_class = serializers.SituacaoUsoBemSerializer
    
class MarcasView(viewsets.ModelViewSet):
    queryset = models.Marcas.objects.all()
    serializer_class = serializers.MarcasSerializer
    
class BensView(viewsets.ModelViewSet):
    queryset = models.Bens.objects.all()
    serializer_class = serializers.BensSerializer
    
