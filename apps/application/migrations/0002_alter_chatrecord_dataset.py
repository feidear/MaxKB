# Generated by Django 4.1.10 on 2023-12-28 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0002_dataset_meta_dataset_type_document_meta_and_more'),
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatrecord',
            name='dataset',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dataset.dataset', verbose_name='数据集'),
        ),
    ]