# Generated by Django 3.1.1 on 2020-09-03 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oddam', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('type', models.CharField(choices=[('FUN', 'Fundacja'), ('ORG', 'organizacja pozarządowa'), ('LOK', 'zbiórka lokalna')], default='FUN', max_length=3)),
                ('categories', models.ManyToManyField(to='oddam.Category')),
            ],
        ),
    ]
