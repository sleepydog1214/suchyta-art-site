# Generated by Django 2.0.6 on 2018-07-09 00:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArtImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=160)),
                ('path', models.FilePathField(path='/documents_1TB_1/thomas/images/opt_svg')),
                ('type', models.CharField(choices=[('JPG', 'Joint Photographic Experts Group'), ('PNG', 'Portable Network Graphics'), ('SVG', 'Scalable Vector Graphics')], max_length=10)),
                ('description', models.TextField()),
                ('height', models.SmallIntegerField()),
                ('width', models.SmallIntegerField()),
                ('date_created', models.DateField(auto_now_add=True)),
                ('last_update', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ArtImageFilters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('type', models.CharField(choices=[('JPG', 'Joint Photographic Experts Group'), ('PNG', 'Portable Network Graphics'), ('SVG', 'Scalable Vector Graphics')], max_length=10)),
                ('description', models.TextField()),
                ('date_created', models.DateField(auto_now_add=True)),
                ('last_update', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('HOME', 'Home'), ('MANIFESTO', 'Manifesto'), ('IMAGES', 'Available Images'), ('PRINT', 'Printer Links'), ('BIO', 'Bio'), ('CONTACT', 'Contact'), ('BLOG', 'Blog')], max_length=25)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('last_update', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PageText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('text', models.TextField()),
                ('date_created', models.DateField(auto_now_add=True)),
                ('last_update', models.DateField(auto_now=True)),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artfilters.Page')),
            ],
        ),
        migrations.CreateModel(
            name='PageTitles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('text', models.TextField()),
                ('date_created', models.DateField(auto_now_add=True)),
                ('last_update', models.DateField(auto_now=True)),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artfilters.Page')),
            ],
        ),
    ]
