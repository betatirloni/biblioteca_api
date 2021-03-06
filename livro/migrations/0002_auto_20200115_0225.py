# Generated by Django 3.0.2 on 2020-01-15 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autor', '0001_initial'),
        ('livro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='disponivel',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='livro',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.RemoveField(
            model_name='livro',
            name='autores',
        ),
        migrations.AddField(
            model_name='livro',
            name='autores',
            field=models.ManyToManyField(to='autor.Autor'),
        ),
    ]
