# Generated by Django 3.0.3 on 2020-02-10 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0007_delete_books'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]