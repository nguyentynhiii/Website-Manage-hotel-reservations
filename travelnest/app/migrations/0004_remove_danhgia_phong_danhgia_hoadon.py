# Generated by Django 4.2.6 on 2023-11-24 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_khachsan_ngay_them'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='danhgia',
            name='phong',
        ),
        migrations.AddField(
            model_name='danhgia',
            name='hoadon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.hoadon'),
        ),
    ]
