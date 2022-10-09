# Generated by Django 4.1 on 2022-09-21 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("shops", "0006_shop1_active"),
    ]

    operations = [
        migrations.AddField(
            model_name="shop1",
            name="menu",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="menu1",
                to="shops.menu",
            ),
        ),
        migrations.AddField(
            model_name="shop1",
            name="service_site",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="service_site",
                to="shops.servicesite",
            ),
        ),
    ]
