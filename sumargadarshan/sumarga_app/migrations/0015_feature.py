# Generated by Django 3.2.5 on 2021-09-16 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sumarga_app', '0014_booksimages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(null=True)),
                ('book_image', models.ImageField(upload_to='pic')),
            ],
        ),
    ]