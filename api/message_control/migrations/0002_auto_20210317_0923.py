# Generated by Django 3.1 on 2021-03-17 09:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('message_control', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='receiver',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='message_receiver', to='user_control.customuser'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='message_sender', to='user_control.customuser'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='messageattachment',
            name='attachment',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='message_uploads', to='message_control.genericfileupload'),
            preserve_default=False,
        ),
    ]
