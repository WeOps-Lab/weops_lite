# Generated by Django 4.2.7 on 2024-03-04 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system_mgmt', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menumanage',
            options={'verbose_name': '菜单管理', 'verbose_name_plural': '菜单管理'},
        ),
        migrations.AlterModelOptions(
            name='operationlog',
            options={'verbose_name': '操作记录', 'verbose_name_plural': '操作记录'},
        ),
        migrations.AlterModelOptions(
            name='syssetting',
            options={'verbose_name': '系统设置', 'verbose_name_plural': '系统设置'},
        ),
        migrations.AlterField(
            model_name='menumanage',
            name='default',
            field=models.BooleanField(default=False, verbose_name='是否是内置菜单'),
        ),
        migrations.AlterField(
            model_name='menumanage',
            name='menu',
            field=models.JSONField(verbose_name='菜单内容'),
        ),
        migrations.AlterField(
            model_name='menumanage',
            name='menu_name',
            field=models.CharField(max_length=64, unique=True, verbose_name='菜单名称'),
        ),
        migrations.AlterField(
            model_name='menumanage',
            name='use',
            field=models.BooleanField(default=False, verbose_name='是否启用(只能有一个)'),
        ),
        migrations.AlterField(
            model_name='operationlog',
            name='app_module',
            field=models.CharField(db_index=True, default='', max_length=20, verbose_name='所属模块'),
        ),
        migrations.AlterField(
            model_name='operationlog',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='operationlog',
            name='obj_type',
            field=models.CharField(db_index=True, default='', max_length=30, verbose_name='对象类型'),
        ),
        migrations.AlterField(
            model_name='operationlog',
            name='operate_obj',
            field=models.CharField(db_index=True, default='', max_length=200, verbose_name='操作对象'),
        ),
        migrations.AlterField(
            model_name='operationlog',
            name='operate_summary',
            field=models.TextField(default='', verbose_name='操作概要'),
        ),
        migrations.AlterField(
            model_name='operationlog',
            name='operate_type',
            field=models.CharField(choices=[('add', '新增'), ('increase', '添加'), ('modify', '修改'), ('exec', '执行'), ('delete', '删除'), ('remove', '移除'), ('download', '下载'), ('upload', '上传'), ('login', '登陆')], db_index=True, max_length=10, verbose_name='操作类型'),
        ),
        migrations.AlterField(
            model_name='operationlog',
            name='operator',
            field=models.CharField(db_index=True, max_length=128, null=True, verbose_name='操作者'),
        ),
    ]
