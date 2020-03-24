# Generated by Django 2.2.11 on 2020-03-20 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("import_data", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="fitbitmember", name="expires_in",),
        migrations.AddField(
            model_name="fitbitmember",
            name="token_expires",
            field=models.DateTimeField(default="2020-03-20 15:45:17+00:00"),
        ),
        migrations.AlterField(
            model_name="fitbitmember",
            name="last_submitted",
            field=models.DateTimeField(default="2020-03-13 15:45:17+00:00"),
        ),
        migrations.AlterField(
            model_name="fitbitmember",
            name="last_updated",
            field=models.DateTimeField(default="2020-03-13 15:45:17+00:00"),
        ),
    ]
