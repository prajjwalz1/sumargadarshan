# Generated by Django 3.2.5 on 2021-10-22 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sumarga_app', '0029_status_bg_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='picks',
            name='category',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='picks',
            name='pages',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='picks',
            name='price',
            field=models.CharField(max_length=40, null=True),
        ),
    ]