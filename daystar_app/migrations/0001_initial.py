# Generated by Django 5.0.4 on 2024-04-24 13:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Baby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baby_id', models.IntegerField(blank=True, null=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('gender', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Sitter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sitter_firstname', models.CharField(max_length=255)),
                ('sitter_lastname', models.CharField(max_length=255)),
                ('sitter_price', models.FloatField()),
                ('start_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='EnrolledStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('baby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='daystar_app.baby')),
                ('sitters', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='daystar_app.sitter')),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
                ('baby', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='daystar_app.baby')),
                ('sitter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='daystar_app.sitter')),
            ],
        ),
    ]
