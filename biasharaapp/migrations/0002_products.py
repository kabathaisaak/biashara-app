# Generated by Django 4.2.7 on 2023-11-07 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biasharaapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField(verbose_name=0)),
                ('description', models.TextField()),
            ],
        ),
    ]
