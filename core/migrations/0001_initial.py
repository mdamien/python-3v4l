# Generated by Django 3.0.5 on 2020-05-02 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Run',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('python_version', models.CharField(max_length=255)),
                ('result', models.TextField()),
                ('run', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Run')),
            ],
        ),
    ]