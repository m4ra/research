# Generated by Django 2.0.2 on 2018-02-06 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=120, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Chapters',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Concept',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(db_index=True, max_length=120, unique=True)),
                ('method', models.TextField(blank=True)),
                ('community', models.CharField(blank=True, max_length=120)),
            ],
            options={
                'verbose_name_plural': 'Concepts',
                'ordering': ('subject',),
            },
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=120, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Fields',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, unique=True)),
                ('publication', models.DateTimeField(blank=True)),
                ('publisher', models.CharField(blank=True, max_length=120)),
                ('authors', models.CharField(blank=True, max_length=120)),
                ('artists', models.CharField(blank=True, max_length=120)),
                ('kind', models.CharField(choices=[('PAPER', 'paper'), ('BOOK', 'book'), ('AUD', 'audio'), ('VID', 'video'), ('ART', 'artwork')], db_index=True, default='PAPER', max_length=5)),
                ('url', models.URLField(blank=True)),
                ('year', models.PositiveIntegerField(db_index=True)),
            ],
            options={
                'verbose_name_plural': 'Materials',
                'ordering': ('title', 'kind', 'year'),
            },
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paragraph', models.TextField()),
                ('material', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='notes', to='phd.Material')),
            ],
            options={
                'verbose_name_plural': 'Notes',
            },
        ),
        migrations.AddField(
            model_name='field',
            name='materials',
            field=models.ManyToManyField(to='phd.Material'),
        ),
        migrations.AddField(
            model_name='concept',
            name='fields',
            field=models.ManyToManyField(to='phd.Field'),
        ),
        migrations.AddField(
            model_name='concept',
            name='meterials',
            field=models.ManyToManyField(to='phd.Material'),
        ),
        migrations.AddField(
            model_name='chapter',
            name='fields',
            field=models.ManyToManyField(to='phd.Field'),
        ),
        migrations.AddField(
            model_name='chapter',
            name='materials',
            field=models.ManyToManyField(to='phd.Material'),
        ),
        migrations.AddField(
            model_name='chapter',
            name='notes',
            field=models.ManyToManyField(to='phd.Note'),
        ),
    ]