# Generated by Django 4.0.2 on 2022-05-31 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Ample', '0008_alter_order_deliverymethod_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reciver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Phone', models.CharField(max_length=20)),
                ('SenderName', models.CharField(max_length=50)),
                ('Address1', models.CharField(max_length=250)),
                ('Address2', models.CharField(max_length=250, null=True)),
                ('State', models.CharField(max_length=50)),
                ('Time', models.DateTimeField(auto_now=True)),
                ('OrderID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ample.order')),
            ],
        ),
    ]
