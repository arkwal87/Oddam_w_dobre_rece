# Generated by Django 3.1.1 on 2020-09-03 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oddam', '0003_donation'),
    ]

    operations = [
        migrations.AddField(
            model_name='institution',
            name='mission',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='institution',
            name='type',
            field=models.CharField(choices=[('FUN', 'Fundacja'), ('ORG', 'Organizacja Pozarządowa'), ('LOK', 'Zbiórka lokalna')], default='FUN', max_length=3),
        ),
    ]
