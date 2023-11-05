# Generated by Django 4.2.6 on 2023-11-03 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collegestore_app', '0002_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='GENDER',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], max_length=255),
        ),
        migrations.AlterField(
            model_name='profile',
            name='PURPOSE',
            field=models.CharField(choices=[('Enquiry', 'Enquiry'), ('Place Order', 'Place Order'), ('Return', 'Return')], max_length=255),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collegestore_app.department')),
            ],
        ),
    ]
