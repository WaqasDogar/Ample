# Generated by Django 4.0.2 on 2022-06-05 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ample', '0014_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='PaymentMehtod',
            field=models.CharField(blank=True, default='Cash on Delivery', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='Description',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='Address2',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='reciver',
            name='Address2',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
