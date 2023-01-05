# Generated by Django 4.1.4 on 2023-01-04 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UWEflix_APP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='register_club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_name', models.CharField(max_length=45)),
                ('club_address_street', models.CharField(max_length=100)),
                ('club_address_street_num', models.CharField(max_length=100)),
                ('club_address_city', models.CharField(max_length=100)),
                ('club_address_postcode', models.CharField(max_length=7)),
                ('club_contact_land_num', models.IntegerField(verbose_name='')),
                ('club_contact_mobile_num', models.IntegerField(verbose_name='')),
                ('club_rep_fname', models.CharField(max_length=30)),
                ('club_rep_lname', models.CharField(max_length=40)),
                ('club_rep_dob', models.DateField()),
                ('club_rep_number', models.IntegerField(verbose_name='')),
                ('club_rep_Pword', models.CharField(max_length=50)),
            ],
        ),
    ]
