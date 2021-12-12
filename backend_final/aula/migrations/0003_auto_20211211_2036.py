# Generated by Django 3.2.9 on 2021-12-11 20:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aula', '0002_fornecedores_projetos_ordens'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bens',
            fields=[
                ('id_bem', models.AutoField(primary_key=True, serialize=False)),
                ('tombamento', models.CharField(max_length=10)),
                ('valor_aquisicao', models.FloatField()),
                ('data_lim_garantia', models.DateField()),
                ('data_fim_garantia', models.DateField()),
                ('data_inicio_uso', models.DateField()),
                ('observacoes', models.TextField()),
                ('dt_cad', models.DateField(auto_now_add=True)),
                ('dt_alt', models.DateField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Bens',
                'db_table': 'Bens',
            },
        ),
        migrations.CreateModel(
            name='EstadosBem',
            fields=[
                ('id_estado_bem', models.AutoField(primary_key=True, serialize=False)),
                ('estado_bem', models.CharField(choices=[('Bom', 'Bom'), ('Regular', 'Regular'), ('Precário', 'Precário'), ('Antieconômico', 'Antieconômico'), ('Inservivel', 'Inservivel')], max_length=80)),
                ('descricao', models.CharField(max_length=255)),
                ('ativo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'EstadoBens',
                'db_table': 'EstadosBem',
                'ordering': ['estado_bem'],
            },
        ),
        migrations.CreateModel(
            name='ItensNotaFiscal',
            fields=[
                ('id_item_nota_fiscal', models.AutoField(primary_key=True, serialize=False)),
                ('qtd', models.PositiveIntegerField()),
                ('valor_unitario', models.FloatField()),
                ('produto_servico', models.CharField(max_length=200)),
                ('dt_cad', models.DateField(auto_now_add=True)),
                ('dt_alt', models.DateField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Item_NotasFiscais',
                'db_table': 'Item_NotasFiscais',
                'ordering': ['id_item_nota_fiscal'],
            },
        ),
        migrations.CreateModel(
            name='Marcas',
            fields=[
                ('id_marca', models.AutoField(primary_key=True, serialize=False)),
                ('marca', models.CharField(max_length=80)),
                ('dt_cad', models.DateField(auto_now_add=True)),
                ('dt_alt', models.DateField(auto_now=True, null=True)),
                ('id_user_alt', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='marcas_user_alt', to=settings.AUTH_USER_MODEL)),
                ('id_user_cad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='marcas_user_cad', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'marcas',
                'db_table': 'Marcas',
                'ordering': ['marca'],
            },
        ),
        migrations.CreateModel(
            name='NotasFiscais',
            fields=[
                ('id_nota_fiscal', models.AutoField(primary_key=True, serialize=False)),
                ('numero', models.PositiveIntegerField()),
                ('ano', models.DateField()),
                ('dt_cad', models.DateField(auto_now_add=True)),
                ('dt_alt', models.DateField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'NotasFiscais',
                'db_table': 'NotasFiscais',
                'ordering': ['id_nota_fiscal'],
            },
        ),
        migrations.CreateModel(
            name='SituacaoUsoBem',
            fields=[
                ('id_situacao_bem', models.AutoField(primary_key=True, serialize=False)),
                ('situacao_uso_bem', models.CharField(choices=[('Em uso', 'Em uso'), ('Em cautela', 'Em cautela'), ('Em manutenção', 'Em manutenção'), ('Em disponibilidade', 'Em disponibilidade'), ('Aguardando', 'Aguardando'), ('Recolhimento', 'Recolhimento'), ('Recolhido', 'Recolhido')], max_length=80)),
                ('descricao', models.CharField(max_length=255)),
                ('ativo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'SituacaoUsoBens',
                'db_table': 'SituacaoUsoBem',
                'ordering': ['situacao_uso_bem'],
            },
        ),
        migrations.RemoveField(
            model_name='projetos',
            name='id_user_alt',
        ),
        migrations.RemoveField(
            model_name='projetos',
            name='id_user_cad',
        ),
        migrations.AlterModelOptions(
            name='fornecedores',
            options={'ordering': ['razao_social'], 'verbose_name_plural': 'Fornecedores'},
        ),
        migrations.AlterModelOptions(
            name='naturezadespesas',
            options={'ordering': ['desc_natureza_despesa'], 'verbose_name_plural': 'Naturezas Despesas'},
        ),
        migrations.AlterModelTable(
            name='fornecedores',
            table='Fornecedores',
        ),
        migrations.AlterModelTable(
            name='naturezadespesas',
            table='NaturezasDespesa',
        ),
        migrations.DeleteModel(
            name='Ordens',
        ),
        migrations.DeleteModel(
            name='Projetos',
        ),
        migrations.AddField(
            model_name='notasfiscais',
            name='id_fornecedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Fornecedor', to='aula.fornecedores'),
        ),
        migrations.AddField(
            model_name='notasfiscais',
            name='id_natureza_despesa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='NaturezaDespesas', to='aula.naturezadespesas'),
        ),
        migrations.AddField(
            model_name='notasfiscais',
            name='id_user_alt',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notasfiscais_user_alt', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='notasfiscais',
            name='id_user_cad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notasfiscais_user_cad', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='itensnotafiscal',
            name='id_nota_fiscal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='NotasFiscais', to='aula.notasfiscais'),
        ),
        migrations.AddField(
            model_name='itensnotafiscal',
            name='id_user_alt',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='itensnotafiscal_user_alt', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='itensnotafiscal',
            name='id_user_cad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itensnotafiscal_user_cad', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bens',
            name='id_estado_bem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='EstadosBem', to='aula.estadosbem'),
        ),
        migrations.AddField(
            model_name='bens',
            name='id_item_nota_fiscal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ItensNotaFiscal', to='aula.itensnotafiscal'),
        ),
        migrations.AddField(
            model_name='bens',
            name='id_marca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Marcas', to='aula.marcas'),
        ),
        migrations.AddField(
            model_name='bens',
            name='id_situacao_uso_bem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='SituacaoUsoBem', to='aula.situacaousobem'),
        ),
        migrations.AddField(
            model_name='bens',
            name='id_user_alt',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bens_user_alt', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bens',
            name='id_user_cad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bens_user_cad', to=settings.AUTH_USER_MODEL),
        ),
    ]