# Generated by Django 4.2.3 on 2023-08-03 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_model', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='father_name',
            field=models.TextField(default='Rahim'),
        ),
    ]