# Generated by Django 5.1.1 on 2024-10-09 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_rename_vote_choice_votes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='votes',
            new_name='vote',
        ),
    ]
