# Generated by Django 4.2 on 2023-05-01 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.IntegerField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('type', models.CharField(choices=[('ACTIVE', 'Active'), ('POTENTIAL', 'Potential'), ('INACTIVE', 'Inactive'), ('PREVIOUS', 'Previous')], default='POTENTIAL', max_length=200)),
            ],
        ),
    ]