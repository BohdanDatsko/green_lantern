# Generated by Django 3.0.7 on 2020-06-05 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsLetter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(max_length=100)),
            ],
            options={
                'verbose_name': 'NewsLetter',
                'verbose_name_plural': 'NewsLetters',
                'ordering': ['email'],
            },
        ),
    ]
