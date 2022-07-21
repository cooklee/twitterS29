# Generated by Django 4.0.6 on 2022-07-21 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter_app', '0006_tweet_urgent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='urgent',
            field=models.IntegerField(choices=[(1, 'nieważne'), (2, 'mało ważne'), (3, 'normal'), (4, 'ważne'), (5, 'Super ważne')], default=3),
        ),
    ]