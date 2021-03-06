# Generated by Django 2.0.6 on 2018-06-22 00:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('imdb_score', models.FloatField(default=0.0)),
                ('popularity99', models.FloatField(default=0.0, help_text='99popularity', verbose_name='99popularity')),
                ('genre', models.ManyToManyField(to='imdb_main.Genre')),
            ],
        ),
        migrations.CreateModel(
            name='MoviePersonRoles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imdb_main.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='MovieRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='moviepersonroles',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imdb_main.Person'),
        ),
        migrations.AddField(
            model_name='moviepersonroles',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imdb_main.MovieRole'),
        ),
        migrations.AddField(
            model_name='movie',
            name='people',
            field=models.ManyToManyField(through='imdb_main.MoviePersonRoles', to='imdb_main.Person'),
        ),
    ]
