# Generated by Django 2.0.8 on 2018-09-06 19:46

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_hotornot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionOpen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField(max_length=250)),
                ('question_videolink', models.CharField(blank=True, max_length=150, null=True)),
                ('question_imagelink', models.CharField(blank=True, max_length=150, null=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='QuestionYesOrNo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField(max_length=250)),
                ('question_videolink', models.CharField(blank=True, max_length=150, null=True)),
                ('question_imagelink', models.CharField(blank=True, max_length=150, null=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserAnswerOpen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_value', models.IntegerField(default=-1, validators=[django.core.validators.MaxValueValidator(2), django.core.validators.MinValueValidator(-1)])),
                ('answer_note', models.TextField(blank=True, max_length=250, null=True)),
                ('first_touched', models.DateTimeField(blank=True, null=True)),
                ('last_touched', models.DateTimeField(auto_now=True)),
                ('count_touched', models.PositiveIntegerField(default=0)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_hotornot.QuestionOpen')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserAnswerYesOrNo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_value', models.IntegerField(default=-1, validators=[django.core.validators.MaxValueValidator(2), django.core.validators.MinValueValidator(-1)])),
                ('answer_note', models.TextField(blank=True, max_length=250, null=True)),
                ('first_touched', models.DateTimeField(blank=True, null=True)),
                ('last_touched', models.DateTimeField(auto_now=True)),
                ('count_touched', models.PositiveIntegerField(default=0)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_hotornot.QuestionYesOrNo')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RenameModel(
            old_name='Question',
            new_name='QuestionMultiple',
        ),
        migrations.RenameModel(
            old_name='UserAnswer',
            new_name='UserAnswerMultiple',
        ),
        migrations.AlterUniqueTogether(
            name='useransweryesorno',
            unique_together={('user', 'question')},
        ),
        migrations.AlterUniqueTogether(
            name='useransweropen',
            unique_together={('user', 'question')},
        ),
    ]
