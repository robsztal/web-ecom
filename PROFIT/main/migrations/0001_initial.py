# Generated by Django 3.1.2 on 2020-10-12 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Magazyn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Produkt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=300)),
                ('complete', models.BooleanField()),
                ('magazyn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.magazyn')),
            ],
        ),
    ]
