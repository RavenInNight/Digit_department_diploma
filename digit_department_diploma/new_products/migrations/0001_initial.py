# Generated by Django 4.2.5 on 2023-09-17 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('new_description', models.TextField()),
                ('new_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('new_quantity', models.PositiveBigIntegerField(default=0)),
                ('new_image_main', models.ImageField(default='', upload_to='products_images')),
                ('new_image_addition', models.ImageField(default='', upload_to='products_images')),
            ],
            options={
                'verbose_name': 'NewProduct',
                'verbose_name_plural': 'NewProducts',
            },
        ),
    ]