# Generated by Django 3.2 on 2022-05-26 13:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fsc_users', '0003_delete_favouriteslist'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fsc_products', '0012_alter_review_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='fsc_users.userprofile'),
        ),
        migrations.CreateModel(
            name='FavouritesList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ManyToManyField(blank=True, to='fsc_products.Product')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]