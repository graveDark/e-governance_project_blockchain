# Generated by Django 3.1.7 on 2021-03-06 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxcalculate', '0002_auto_20210306_1403'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='govt',
            name='id',
        ),
        migrations.AddField(
            model_name='govt',
            name='tax_amt',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='govt',
            name='uid',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]