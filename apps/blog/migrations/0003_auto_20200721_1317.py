# Generated by Django 2.2.8 on 2020-07-21 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200719_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(default='AICodeLab是一个使用 Django+Bootstrap4 搭建的个人博客类型网站', help_text='用来作为SEO中description,长度参考SEO标准', max_length=240, verbose_name='描述'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='description',
            field=models.TextField(default='AICodeLab是一个使用 Django+Bootstrap4 搭建的个人博客类型网站', help_text='用来作为SEO中description,长度参考SEO标准', max_length=240, verbose_name='描述'),
        ),
    ]
