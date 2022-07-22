# Generated by Django 4.0.2 on 2022-05-29 20:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Ample', '0005_delete_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(default='images/default.png', upload_to='images/')),
                ('UserType', models.CharField(choices=[('Admin', 'ADMIN'), ('Customer', 'CUSTOMER'), ('Driver', 'DRIVER')], max_length=50)),
                ('Address', models.CharField(max_length=150)),
                ('Time', models.DateTimeField(auto_now=True)),
                ('UserID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]