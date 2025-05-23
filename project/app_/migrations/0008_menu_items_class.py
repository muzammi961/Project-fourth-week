# Generated by Django 5.1.6 on 2025-03-24 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_', '0007_alter_registration_class_password_registr'),
    ]

    operations = [
        migrations.CreateModel(
            name='menu_items_class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=100, unique=True)),
                ('price', models.IntegerField(max_length=255)),
                ('offer_price', models.ImageField(upload_to='')),
                ('time_set', models.DateTimeField(auto_now=True)),
                ('profile_photo', models.ImageField(upload_to='menu_photo')),
            ],
        ),
    ]
