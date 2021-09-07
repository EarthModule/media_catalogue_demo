# Generated by Django 3.2.7 on 2021-09-07 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512)),
                ('year', models.DateField()),
                ('box_office', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MovieCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='MovieStaffMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('birth_year', models.DateField(blank=True, null=True)),
                ('is_alive', models.BooleanField(default=True)),
                ('career', models.CharField(choices=[('DRT', 'Director'), ('ACT', 'Actor')], default='ACT', max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='MovieRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=512)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roles', to='movies.moviestaffmember')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_roles', to='movies.movie')),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(related_name='actors', to='movies.MovieStaffMember'),
        ),
        migrations.AddField(
            model_name='movie',
            name='categories',
            field=models.ManyToManyField(related_name='categories', to='movies.MovieCategory'),
        ),
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='director', to='movies.moviestaffmember'),
        ),
    ]