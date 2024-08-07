# Generated by Django 4.2.7 on 2024-07-24 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Node",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_by",
                    models.CharField(default="", max_length=32, verbose_name="创建者"),
                ),
                (
                    "updated_by",
                    models.CharField(default="", max_length=32, verbose_name="更新者"),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, db_index=True, verbose_name="创建时间"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="修改时间"),
                ),
                (
                    "model_id",
                    models.CharField(
                        db_index=True, max_length=100, verbose_name="模型ID"
                    ),
                ),
                ("node_id", models.BigIntegerField(unique=True, verbose_name="节点ID")),
                ("node_name", models.CharField(max_length=100, verbose_name="节点名称")),
                ("node_ip", models.CharField(max_length=100, verbose_name="IP地址")),
                (
                    "sidecar_status",
                    models.CharField(
                        default="not_installed",
                        max_length=100,
                        verbose_name="sidecar状态",
                    ),
                ),
                ("sidecar_sync_time", models.DateTimeField(verbose_name="sidecar同步时间")),
                (
                    "sidecar_config",
                    models.JSONField(default=dict, verbose_name="sidecar配置信息"),
                ),
            ],
            options={
                "verbose_name": "时间相关字段",
                "abstract": False,
            },
        ),
    ]
