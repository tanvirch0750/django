# Generated by Django 4.2.3 on 2023-08-10 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_model', '0009_student2_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='student',
            field=models.ManyToManyField(related_name='teachers', to='django_model.student2'),
        ),
    ]
