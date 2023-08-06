# Generated by Django 4.2.3 on 2023-08-06 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_model', '0007_person_alter_me_options_passport'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_cap', models.CharField(max_length=50)),
                ('post_details', models.CharField(max_length=100)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='django_model.person')),
            ],
        ),
    ]
