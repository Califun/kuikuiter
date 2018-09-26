# Generated by Django 2.1.1 on 2018-09-20 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('text', models.CharField(default='', max_length=1024)),
                ('like_counter', models.IntegerField(default=0)),
            ],
        ),
    ]
