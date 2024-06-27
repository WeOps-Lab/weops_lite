# Generated by Django 4.2.7 on 2024-06-27 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cmdb_mgmt", "0007_alter_rolecredentialpermission_inst_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rolecredentialpermission",
            name="inst_id",
            field=models.BigIntegerField(db_index=True, verbose_name="凭据实例ID"),
        ),
        migrations.AlterField(
            model_name="usercredentialpermission",
            name="inst_id",
            field=models.BigIntegerField(db_index=True, verbose_name="凭据实例ID"),
        ),
    ]