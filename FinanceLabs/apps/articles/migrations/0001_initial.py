# Generated by Django 3.0.3 on 2020-03-09 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=100, verbose_name='Назва статті')),
                ('article_text', models.TextField(verbose_name='Текст статті')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='Дата публікації')),
                ('article_rate', models.FloatField(default=0.0, verbose_name='Рейтинг статті')),
            ],
            options={
                'verbose_name': 'Стаття',
                'verbose_name_plural': 'Статті',
            },
        ),
        migrations.CreateModel(
            name='Indicator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kvartal', models.DecimalField(decimal_places=0, max_digits=1, verbose_name='Квартал')),
                ('year', models.CharField(max_length=4, verbose_name='Рік')),
                ('E', models.DecimalField(decimal_places=0, max_digits=5, verbose_name='Сумарні постійні витрати')),
                ('C', models.DecimalField(decimal_places=0, max_digits=5, verbose_name='Сумарні змінні витрати')),
                ('V', models.DecimalField(decimal_places=0, max_digits=5, verbose_name='Обєм продаж')),
            ],
            options={
                'verbose_name': 'Показник ефективності',
                'verbose_name_plural': 'Показники ефективності',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=50, verbose_name='Ім*я автора')),
                ('comment_text', models.CharField(max_length=200, verbose_name='Текст коментаря')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Article')),
            ],
            options={
                'verbose_name': 'Коментарій',
                'verbose_name_plural': 'Коментарі',
            },
        ),
    ]
