# Generated by Django 4.2.1 on 2024-04-25 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_snippet'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sport_Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=20)),
                ('speed', models.IntegerField(default=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Snippet',
        ),
        migrations.RemoveField(
            model_name='student',
            name='file',
        ),
        migrations.RemoveField(
            model_name='student',
            name='image',
        ),
    ]
