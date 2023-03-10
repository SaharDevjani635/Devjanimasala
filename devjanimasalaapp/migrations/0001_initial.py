# Generated by Django 4.1.7 on 2023-02-24 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('product_image', models.ImageField(upload_to='./products')),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('products_featured', models.BooleanField()),
                ('product_details', models.TextField(max_length=1200)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='devjanimasalaapp.category')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_review', models.TextField(max_length=500)),
                ('product_ratings', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('8', '5')], max_length=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating', to='devjanimasalaapp.product')),
            ],
        ),
    ]
