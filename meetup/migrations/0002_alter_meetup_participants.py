# Generated by Django 3.2.9 on 2021-11-09 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetup',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='partcipant_name', to='meetup.Participant'),
        ),
    ]