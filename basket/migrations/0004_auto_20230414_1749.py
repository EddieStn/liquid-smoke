# Generated by Django 3.2 on 2023-04-14 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_review_approved'),
        ('basket', '0003_alter_basketitem_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='basketitem',
            name='discounted_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='basketitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product'),
        ),
    ]
