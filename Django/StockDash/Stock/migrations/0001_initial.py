# Generated by Django 3.0.4 on 2020-04-06 23:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RealTimeData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_time', models.TimeField()),
                ('real_price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='StockInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('st_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='DayData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_date', models.DateField()),
                ('close_price', models.FloatField()),
                ('netchg', models.FloatField()),
                ('chg_price', models.FloatField()),
                ('stockinfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Stock.StockInfo')),
            ],
        ),
    ]
