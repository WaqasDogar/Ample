# Generated by Django 4.0.2 on 2022-07-18 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ample', '0019_alter_order_status_reassign'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='Reason',
            field=models.CharField(blank=True, default='Empty', max_length=100, null=True),
        ),
    ]
