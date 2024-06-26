# Generated by Django 4.2.7 on 2024-06-16 12:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Category')),
                ('slug', models.SlugField(blank=True, max_length=255, verbose_name='URL category')),
                ('description', models.TextField(max_length=300, verbose_name='Category description')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='article.category', verbose_name='Parent category')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Slug')),
                ('title', models.CharField(max_length=255, verbose_name='Heading')),
                ('content', models.TextField(blank=True, verbose_name='Article text')),
                ('photo', models.ImageField(blank=True, default=None, null=True, upload_to='photos/%Y/%m/%d/', verbose_name='Photo')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Time of creation')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Change time')),
                ('is_published', models.BooleanField(default=True, verbose_name='is_published')),
                ('author', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='tasks_author', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('cat', mptt.fields.TreeForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='articles', to='article.category', verbose_name='Category')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'Dog breeds',
                'verbose_name_plural': 'Dog breeds',
                'ordering': ['-time_create'],
                'indexes': [models.Index(fields=['-time_create'], name='article_art_time_cr_f21e29_idx')],
            },
        ),
    ]
