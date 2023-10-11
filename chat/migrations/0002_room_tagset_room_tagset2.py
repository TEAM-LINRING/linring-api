# Generated by Django 4.2.3 on 2023-10-09 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='tagset',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, related_name='room_tagset', to='accounts.tagset', verbose_name='태그셋1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='tagset2',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, related_name='room_tagset2', to='accounts.tagset', verbose_name='태그셋2'),
            preserve_default=False,
        ),
    ]
