# Generated by Django 3.2.7 on 2021-09-06 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog_config", "0002_blogdata"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="blogdata",
            name="nome",
        ),
        migrations.AddField(
            model_name="blogdata",
            name="name",
            field=models.CharField(default=0, max_length=50, verbose_name="name"),
            preserve_default=False,
        ),
    ]