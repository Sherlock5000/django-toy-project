# Generated by Django 3.0 on 2021-06-17 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='note',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Indoor', 'Indoor'), ('Out Door', 'Out Door')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(to='accounts.Tag'),
        ),
    ]
