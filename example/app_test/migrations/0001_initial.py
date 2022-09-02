# Generated by Django 3.2.14 on 2022-09-02 21:27

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
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('users', models.ManyToManyField(related_name='tenants', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_test.category')),
                ('tenant', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='app_test.customer')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='category',
            name='tenant',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='app_test.customer'),
        ),
    ]
