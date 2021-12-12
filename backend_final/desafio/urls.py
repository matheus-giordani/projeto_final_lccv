"""desafio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


from rest_framework import routers
from aula import views

router = routers.DefaultRouter()
router.register(r'natureza_despesas', views.NaturezaDespesasView)
router.register(r'fornecedores', views.FornecedoresView)
router.register(r'notas_fiscais', views.NotasFiscaisView)
router.register(r'itens_notafiscal', views.ItensNotaFiscalView)
router.register(r'estados_bem', views.EstadosBemView)
router.register(r'situacao_usobem', views.SituacaoUsoBemView)
router.register(r'marcas', views.MarcasView)
router.register(r'bens', views.BensView)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    
]
