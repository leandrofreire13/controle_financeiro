# Generated by Django 3.2.8 on 2021-11-23 13:19

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Gasto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=200)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=6)),
                ('vencimento', models.DateField(default=datetime.time)),
                ('status', models.CharField(choices=[('Comprado', 'COMPRADO'), ('Lançado na fatura', 'LANCADO_NA_FATURA'), ('Pago', 'PAGO')], default='Comprado', max_length=200)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.categoria')),
            ],
        ),
    ]