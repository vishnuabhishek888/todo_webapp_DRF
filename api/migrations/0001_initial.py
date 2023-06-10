# Generated by Django 4.2.2 on 2023-06-10 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('due_date', models.DateField(blank=True)),
                ('tags', models.CharField(blank=True, max_length=20)),
                ('status', models.CharField(choices=[('open', 'Open'), ('working', 'Working'), ('done', 'Done'), ('overdue', 'Overdeue')], default='open', max_length=20)),
            ],
        ),
    ]
