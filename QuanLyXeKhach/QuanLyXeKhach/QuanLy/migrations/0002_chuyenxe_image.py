# Generated by Django 4.1.7 on 2023-03-22 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuanLy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chuyenxe',
            name='image',
            field=models.ImageField(null=True, upload_to='QuanLy/%Y/%m'),
        ),
    ]
