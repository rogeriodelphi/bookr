# Generated by Django 4.0.1 on 2022-01-25 04:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookContributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('AUTHOR', 'Author'), ('CO_AUTHOR', 'Co-Author'), ('EDITOR', 'Editor')], max_length=20, verbose_name='The role this contributor had in the book.')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='contributors',
            field=models.ManyToManyField(through='reviews.BookContributor', to='reviews.Contributor'),
        ),
        migrations.AddField(
            model_name='bookcontributor',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.book'),
        ),
        migrations.AddField(
            model_name='bookcontributor',
            name='contributor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.contributor'),
        ),
    ]
