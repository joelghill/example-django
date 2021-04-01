# Generated by Django 3.0.12 on 2021-03-23 02:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0003_auto_20210322_1901'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=250)),
                ('postal_code', models.CharField(max_length=6)),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='people.Address'),
        ),
    ]
