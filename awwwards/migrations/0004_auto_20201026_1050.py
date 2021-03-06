# Generated by Django 3.1.2 on 2020-10-26 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awwwards', '0003_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='rate',
        ),
        migrations.AddField(
            model_name='review',
            name='rate_content',
            field=models.PositiveIntegerField(choices=[(1, '1 - awful2'), (2, '2 - Horrible'), (3, '3 - Terrible'), (4, '4 - Bad'), (5, '5 - OK'), (6, '6 - nice work'), (7, '7 - Good'), (8, '8 - Very Good'), (9, '9 - Perfect'), (10, '10 - Masterpiece')], null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='rate_design',
            field=models.PositiveSmallIntegerField(choices=[(1, '1 - awful2'), (2, '2 - Horrible'), (3, '3 - Terrible'), (4, '4 - Bad'), (5, '5 - OK'), (6, '6 - nice work'), (7, '7 - Good'), (8, '8 - Very Good'), (9, '9 - Perfect'), (10, '10 - Masterpiece')], null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='rate_usage',
            field=models.PositiveSmallIntegerField(choices=[(1, '1 - awful2'), (2, '2 - Horrible'), (3, '3 - Terrible'), (4, '4 - Bad'), (5, '5 - OK'), (6, '6 - nice work'), (7, '7 - Good'), (8, '8 - Very Good'), (9, '9 - Perfect'), (10, '10 - Masterpiece')], null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
