# Generated by Django 4.1.9 on 2023-10-16 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_projectimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectimage',
            name='caption',
            field=models.CharField(blank=True, help_text='Add a caption to the image.', max_length=100, null=True, verbose_name='Caption'),
        ),
    ]
