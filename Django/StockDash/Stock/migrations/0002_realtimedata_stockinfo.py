# Generated by Django 3.0.4 on 2020-04-07 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Stock', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='realtimedata',
            name='stockinfo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Stock.StockInfo'),
            preserve_default=False,
        ),
    ]