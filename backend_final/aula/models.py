from django.db import models
from django.contrib.auth.models import User

from django import forms

# Create your models here.






class NaturezaDespesas(models.Model):
    id_natureza_despesa = models.AutoField(primary_key=True)
    cod_natureza_despesa = models.CharField(max_length=8)
    desc_natureza_despesa = models.CharField(max_length=60)
    
    class Meta:
        ordering = ["desc_natureza_despesa"]
        db_table = "NaturezasDespesa"
        verbose_name_plural = "Naturezas Despesas"

    def __str__(self) -> str:
        return self.desc_natureza_despesa
    

  
class Fornecedores(models.Model):
    id_fornecedor = models.AutoField(primary_key=True)
    razao_social = models.CharField(max_length= 200)
    cnpj = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50)
    telefone = models.CharField(max_length=50)
    id_user_cad = models.ForeignKey(User,on_delete=models.CASCADE, related_name='%(class)s_user_cad')
    dt_cad = models.DateField(auto_now_add=True)
    id_user_alt = models.ForeignKey(User,on_delete=models.CASCADE, related_name='%(class)s_user_alt', null=True)
    dt_alt = models.DateField(null=True, blank=True, auto_now=True)
    class Meta:
        ordering = ['razao_social']
        db_table = "Fornecedores"
        verbose_name_plural = 'Fornecedores'

    def __str__(self) -> str:
        return self.razao_social 

    
class NotasFiscais(models.Model):
    id_nota_fiscal = models.AutoField(primary_key=True)
    id_fornecedor = models.ForeignKey(Fornecedores, on_delete=models.CASCADE, related_name= 'Fornecedor')
    id_natureza_despesa = models.ForeignKey(NaturezaDespesas, on_delete=models.CASCADE, related_name = 'NaturezaDespesas')
    numero = models.PositiveIntegerField()
    ano = models.PositiveIntegerField(null = True)
    id_user_cad = models.ForeignKey(User,on_delete=models.CASCADE, related_name='%(class)s_user_cad')
    dt_cad = models.DateField(auto_now_add=True)
    id_user_alt = models.ForeignKey(User,on_delete=models.CASCADE, related_name='%(class)s_user_alt', null=True)
    dt_alt = models.DateField(null=True, blank=True, auto_now=True)
    class Meta:
        ordering = ['id_nota_fiscal']
        db_table = "NotasFiscais"
        verbose_name_plural = 'NotasFiscais'
    
    
    def __str__(self)-> str:
        return self.id_fornecedor.razao_social + '-' + str(self.numero)
    
    
    
class ItensNotaFiscal(models.Model):
    id_item_nota_fiscal = models.AutoField(primary_key=True)
    id_nota_fiscal = models.ForeignKey(NotasFiscais, on_delete=models.CASCADE, related_name= 'NotasFiscais')
    qtd = models.PositiveIntegerField()
    valor_unitario = models.FloatField()
    produto_servico = models.CharField(max_length=200)
    id_user_cad = models.ForeignKey(User,on_delete=models.CASCADE, related_name='%(class)s_user_cad')
    dt_cad = models.DateField(auto_now_add=True)
    id_user_alt = models.ForeignKey(User,on_delete=models.CASCADE, related_name='%(class)s_user_alt', null=True)
    dt_alt = models.DateField(null=True, blank=True, auto_now=True)
    class Meta:
        ordering = ['id_item_nota_fiscal']
        db_table = "Item_NotasFiscais"
        verbose_name_plural = 'Item_NotasFiscais'
    
    
    def __str__(self)-> str:
        return self.produto_servico + '-' + str(self.id_item_nota_fiscal)
    
class EstadosBem(models.Model):
    id_estado_bem = models.AutoField(primary_key=True)
    CHOICES_1 = (('Bom', 'Bom'), 
                 ('Regular', 'Regular'), 
                 ('Precário','Precário'), 
                 ('Antieconômico', 'Antieconômico'), 
                 ('Inservivel', 'Inservivel'))
    estado_bem = models.CharField(max_length=80,choices = CHOICES_1)
    descricao = models.CharField(max_length=255)
    ativo = models.BooleanField(default= True)
    class Meta:
        ordering = ['estado_bem']
        db_table = "EstadosBem"
        verbose_name_plural = 'EstadoBens'
    
    
    def __str__(self)-> str:
        return self.descricao
    
    
    
    
class SituacaoUsoBem(models.Model):
    id_situacao_bem = models.AutoField(primary_key=True)
    CHOICES_2 = (('Em uso','Em uso'),
               ('Em cautela','Em cautela'),
               ('Em manutenção','Em manutenção'),
               ('Em disponibilidade','Em disponibilidade'),
               ('Aguardando','Aguardando'),
               ('Recolhimento','Recolhimento'),
               ('Recolhido','Recolhido'))
    situacao_uso_bem = models.CharField(max_length=80,choices = CHOICES_2)
    descricao = models.CharField(max_length=255)
    ativo = models.BooleanField(default= True)
    class Meta:
        ordering = ['situacao_uso_bem']
        db_table = "SituacaoUsoBem"
        verbose_name_plural = 'SituacaoUsoBens'
    
    
    def __str__(self)-> str:
        return self.descricao
    
    
class Marcas(models.Model):
    id_marca = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=80)
    id_user_cad = models.ForeignKey(User,on_delete=models.CASCADE, related_name='%(class)s_user_cad')
    dt_cad = models.DateField(auto_now_add=True)
    id_user_alt = models.ForeignKey(User,on_delete=models.CASCADE, related_name='%(class)s_user_alt', null=True)
    dt_alt = models.DateField(null=True, blank=True, auto_now=True)
    
    class Meta:
        ordering = ['marca']
        db_table = "Marcas"
        verbose_name_plural = 'marcas'
    
    
    def __str__(self)-> str:
        return str(self.id_marca) + '-' + self.marca
    
    
    
class Bens(models.Model):
    id_bem = models.AutoField(primary_key=True)
    id_item_nota_fiscal = models.ForeignKey(ItensNotaFiscal, on_delete=models.CASCADE, related_name= 'ItensNotaFiscal')
    tombamento = models.CharField(max_length=10)
    id_estado_bem = models.ForeignKey(EstadosBem, on_delete=models.CASCADE, related_name= 'EstadosBem')
    id_situacao_uso_bem =  models.ForeignKey(SituacaoUsoBem, on_delete=models.CASCADE, related_name= 'SituacaoUsoBem')
    valor_aquisicao = models.FloatField()
    id_marca =  models.ForeignKey(Marcas, on_delete=models.CASCADE, related_name= 'Marcas')
    data_lim_garantia = models.DateField()
    data_fim_garantia = models.DateField()
    data_inicio_uso = models.DateField()
    observacoes = models.TextField()
    id_user_cad = models.ForeignKey(User,on_delete=models.CASCADE, related_name='%(class)s_user_cad')    
    dt_cad = models.DateField(auto_now_add=True)
    id_user_alt = models.ForeignKey(User,on_delete=models.CASCADE, related_name='%(class)s_user_alt', null=True)
    dt_alt = models.DateField(null=True, blank=True, auto_now=True)
    
    class Meta:
        
        db_table = "Bens"
        verbose_name_plural = 'Bens'
    
    
    def __str__(self)-> str:
        return self.tombamento
    