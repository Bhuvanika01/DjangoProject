# Generated by Django 4.2.3 on 2023-08-02 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0002_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='products',
            name='tags',
            field=models.ManyToManyField(to='calc.tag'),
        ),
    ]
