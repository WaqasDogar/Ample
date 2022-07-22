# Generated by Django 4.0.2 on 2022-05-31 19:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Ample', '0006_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DeliveryMethod', models.CharField(choices=[('Delivery with Cooler', 'DELIVERY WITH COOLER'), ('Normal Delivery', 'NORMAL DELIVERY'), ('Driver', 'DRIVER')], max_length=50)),
                ('Phone', models.CharField(max_length=20)),
                ('SenderName', models.CharField(max_length=50)),
                ('Address1', models.CharField(max_length=250)),
                ('Address2', models.CharField(max_length=250, null=True)),
                ('State', models.CharField(max_length=50)),
                ('TodayDate', models.DateField(auto_now=True)),
                ('DeliveryDate', models.DateField()),
                ('Time', models.DateTimeField(auto_now=True)),
                ('UserID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]