# Generated by Django 4.0.3 on 2022-03-10 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='login_method',
            field=models.CharField(choices=[('email', 'Email'), ('kakao', 'Kakao')], default='email', max_length=20),
        ),
    ]