# Generated by Django 4.0.2 on 2022-02-09 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_text_comment_text_de'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='text_en',
            field=models.CharField(default='text some', max_length=100),
            preserve_default=False,
        ),
    ]
