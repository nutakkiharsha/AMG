# Generated by Django 3.0.5 on 2020-08-06 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0016_auto_20200804_1833'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pickUpPlace', models.CharField(max_length=105, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='pickUpPlace',
        ),
        migrations.AddField(
            model_name='order',
            name='pickUp',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='website.Location'),
        ),
    ]
