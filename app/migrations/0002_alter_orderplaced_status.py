# Generated by Django 4.0.3 on 2022-05-18 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Xác nhận', 'Xác nhận'), ('Đóng gói', 'Đóng gói'), ('Vận chuyển', 'Vận chuyển'), ('Đã giao hàng', 'Đã giao hàng'), ('Hủy đơn hàng', 'Hủy đơn hàng')], default='Chờ xử lý', max_length=50),
        ),
    ]
