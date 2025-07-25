# Generated by Django 5.2.3 on 2025-07-03 09:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
        ('stats', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='incomeproduct',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='sale',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.branch'),
        ),
        migrations.AddField(
            model_name='sale',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.customer'),
        ),
        migrations.AddField(
            model_name='sale',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product'),
        ),
        migrations.AddField(
            model_name='sale',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
