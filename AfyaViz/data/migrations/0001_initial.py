# Generated by Django 4.2.3 on 2024-03-23 06:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('description', models.TextField(blank=True)),
                ('uploaded_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='DataSource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, unique=True)),
                ('description', models.TextField(blank=True)),
                ('contact_info', models.CharField(blank=True, max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Variable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('description', models.TextField(blank=True)),
                ('variable_type', models.CharField(choices=[('Numeric', 'Numeric'), ('Categorical', 'Categorical'), ('Date', 'Date')], max_length=255)),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.dataset')),
            ],
        ),
        migrations.AddField(
            model_name='dataset',
            name='data_source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.datasource'),
        ),
        migrations.CreateModel(
            name='DataPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entity_id', models.IntegerField(blank=True, null=True)),
                ('value', models.TextField()),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.dataset')),
                ('variable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.variable')),
            ],
        ),
    ]