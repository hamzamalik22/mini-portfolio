# Generated by Django 5.0.7 on 2024-07-29 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_project_options_project_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='date',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
