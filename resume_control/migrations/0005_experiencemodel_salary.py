# Generated by Django 4.1.4 on 2023-05-04 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_control', '0004_alter_experiencemodel_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiencemodel',
            name='salary',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
