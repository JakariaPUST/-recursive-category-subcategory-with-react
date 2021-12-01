# Generated by Django 3.2.4 on 2021-11-30 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_a_b'),
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='base.node')),
            ],
            options={
                'verbose_name_plural': 'Nodes',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
            ],
            options={
                'verbose_name_plural': 'Categories',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('base.node',),
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
            ],
            options={
                'verbose_name_plural': 'Sub Categories',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('base.node',),
        ),
        migrations.CreateModel(
            name='SubSubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155)),
                ('sub_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.subcategory')),
            ],
        ),
    ]
