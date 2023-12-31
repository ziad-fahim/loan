# Generated by Django 3.2.7 on 2023-12-29 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='programs',
            old_name='max_length',
            new_name='max_amount',
        ),
        migrations.AddField(
            model_name='programs',
            name='max_age',
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='programs',
            name='min_age',
            field=models.IntegerField(default=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='status',
            field=models.CharField(blank=True, choices=[(1, 'Approved'), (2, 'Rejected')], max_length=10, null=True),
        ),
    ]
