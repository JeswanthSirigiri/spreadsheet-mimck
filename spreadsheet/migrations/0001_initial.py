# Generated by Django 4.2.14 on 2025-02-26 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Spreadsheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row', models.IntegerField()),
                ('col', models.IntegerField()),
                ('value', models.CharField(blank=True, max_length=255, null=True)),
                ('formula', models.CharField(blank=True, max_length=255, null=True)),
                ('spreadsheet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cells', to='spreadsheet.spreadsheet')),
            ],
            options={
                'unique_together': {('spreadsheet', 'row', 'col')},
            },
        ),
    ]
