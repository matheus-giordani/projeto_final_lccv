from django.contrib import admin
from . import models
from . import actions
# Register your models here.
class BaseForm(admin.ModelAdmin):
    readonly_fields = ['id_user_cad','id_user_alt']
    
    
    
    def save_model(self, request,obj,form,change):
        if change:
            obj.id_user_alt = request.user
        else:
            obj.id_user_cad   = request.user
        obj.save()
        
class FornecedorForm(BaseForm):
    search_fields = ['razao_social', 'cnpj', 'email', 'telefone']
    list_filter = ['razao_social']

admin.site.register(models.NaturezaDespesas, )
admin.site.register(models.Bens, BaseForm)
admin.site.register(models.EstadosBem)
admin.site.register(models.ItensNotaFiscal, BaseForm)
admin.site.register(models.Marcas, BaseForm)
admin.site.register(models.NotasFiscais, BaseForm)
admin.site.register(models.SituacaoUsoBem)
admin.site.register(models.Fornecedores, FornecedorForm)
