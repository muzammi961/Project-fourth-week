# Generated by Django 5.1.7 on 2025-03-21 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration_class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_registr', models.CharField(max_length=100)),
                ('phone_number_registr', models.IntegerField(max_length=100)),
                ('gmail_person_registr', models.EmailField(max_length=254, unique=True)),
                ('password_registr', models.EmailField(max_length=254, unique=True)),
            ],
        ),
    ]
