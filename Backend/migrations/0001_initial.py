# Generated by Django 5.0.4 on 2024-05-03 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriesDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_category', models.CharField(blank=True, max_length=100, null=True)),
                ('Des_category', models.CharField(blank=True, max_length=200, null=True)),
                ('Img_category', models.ImageField(blank=True, null=True, upload_to='CategoryImages')),
            ],
        ),
    ]
