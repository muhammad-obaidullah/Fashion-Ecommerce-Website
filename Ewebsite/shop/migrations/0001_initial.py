# Generated by Django 3.1 on 2020-08-16 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('desc', models.CharField(max_length=3000)),
                ('collection_name', models.CharField(default='', max_length=100)),
                ('image', models.ImageField(default='', upload_to='shop/images')),
            ],
        ),
    ]