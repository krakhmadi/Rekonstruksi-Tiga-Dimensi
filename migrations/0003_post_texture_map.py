# Generated by Django 3.1.5 on 2021-01-30 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rekonstruksi', '0002_post_html'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='texture_map',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
