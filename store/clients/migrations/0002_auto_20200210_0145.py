# Generated by Django 3.0.3 on 2020-02-09 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='product_image',
        ),
        migrations.AlterField(
            model_name='books',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.Products'),
        ),
    ]