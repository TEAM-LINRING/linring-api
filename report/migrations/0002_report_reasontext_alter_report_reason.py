# Generated by Django 4.2.3 on 2023-10-08 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='ReasonText',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='신고 사유 입력'),
        ),
        migrations.AlterField(
            model_name='report',
            name='Reason',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=100, verbose_name='신고 사유'),
        ),
    ]
