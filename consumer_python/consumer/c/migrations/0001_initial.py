# Generated by Django 2.0.5 on 2018-05-19 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Msg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg_text', models.CharField(max_length=200)),
                ('msg_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
