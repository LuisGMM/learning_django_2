# Generated by Django 4.1.5 on 2023-01-10 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_cart_id_alter_cartitem_cart'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cartitem',
            unique_together={('cart', 'product')},
        ),
    ]