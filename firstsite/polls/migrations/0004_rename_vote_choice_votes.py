# Generated by Django 5.1.1 on 2024-10-09 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_rename_votes_choice_vote'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='vote',
            new_name='votes',
        ),
    ]
