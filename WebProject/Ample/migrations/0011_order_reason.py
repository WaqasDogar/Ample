# Generated by Django 4.0.2 on 2022-06-01 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ample', '0010_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='Reason',
            field=models.CharField(blank=True, default='Empty', max_length=100, null=True),
        ),
    ]