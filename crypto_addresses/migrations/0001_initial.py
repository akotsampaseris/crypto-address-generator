# Generated by Django 4.1.1 on 2022-10-01 23:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('crypto_coins', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CryptoAddress',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('coin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crypto_coins.cryptocoin')),
            ],
        ),
    ]
