# Generated by Django 4.1 on 2022-09-30 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0007_alter_order_shop"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="deleted_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]