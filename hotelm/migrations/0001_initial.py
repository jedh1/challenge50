# Generated by Django 3.0.7 on 2020-06-16 23:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipient', models.CharField(blank=True, max_length=100)),
                ('destination', models.CharField(max_length=128)),
                ('check_in', models.CharField(max_length=16)),
                ('check_out', models.CharField(max_length=16)),
                ('special_rates', models.CharField(blank=True, max_length=32)),
                ('special_rates_code', models.CharField(blank=True, max_length=16)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('recurrence', models.IntegerField(default=0)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]