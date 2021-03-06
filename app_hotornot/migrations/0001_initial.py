# Generated by Django 2.0.8 on 2018-09-10 17:52

from django.conf import settings
import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField(max_length=250)),
                ('question_videolink', models.CharField(blank=True, max_length=150, null=True)),
                ('question_imagelink', models.CharField(blank=True, max_length=150, null=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserAnswerMultiple',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_touched', models.DateTimeField(blank=True, null=True)),
                ('last_touched', models.DateTimeField(auto_now=True)),
                ('count_touched', models.PositiveIntegerField(default=0)),
                ('answer_choice_key', models.IntegerField(default=-1, validators=[django.core.validators.MinValueValidator(0)])),
                ('user', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserAnswerOpen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_touched', models.DateTimeField(blank=True, null=True)),
                ('last_touched', models.DateTimeField(auto_now=True)),
                ('count_touched', models.PositiveIntegerField(default=0)),
                ('answer_text', models.TextField(blank=True, max_length=250, null=True)),
                ('user', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserAnswerYesOrNo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_touched', models.DateTimeField(blank=True, null=True)),
                ('last_touched', models.DateTimeField(auto_now=True)),
                ('count_touched', models.PositiveIntegerField(default=0)),
                ('answer_value', models.IntegerField(default=-1, validators=[django.core.validators.MaxValueValidator(2), django.core.validators.MinValueValidator(0)])),
                ('answer_note', models.TextField(blank=True, max_length=250, null=True)),
                ('user', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='QuestionMultiple',
            fields=[
                ('question_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app_hotornot.Question')),
                ('options', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=150), default=list, null=True, size=4)),
            ],
            bases=('app_hotornot.question',),
        ),
        migrations.CreateModel(
            name='QuestionOpen',
            fields=[
                ('question_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app_hotornot.Question')),
            ],
            bases=('app_hotornot.question',),
        ),
        migrations.CreateModel(
            name='QuestionYesOrNo',
            fields=[
                ('question_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app_hotornot.Question')),
            ],
            bases=('app_hotornot.question',),
        ),
        migrations.AddField(
            model_name='useransweryesorno',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_hotornot.QuestionYesOrNo'),
        ),
        migrations.AddField(
            model_name='useransweropen',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_hotornot.QuestionOpen'),
        ),
        migrations.AddField(
            model_name='useranswermultiple',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_hotornot.QuestionMultiple'),
        ),
        migrations.AlterUniqueTogether(
            name='useransweryesorno',
            unique_together={('user', 'question')},
        ),
        migrations.AlterUniqueTogether(
            name='useransweropen',
            unique_together={('user', 'question')},
        ),
        migrations.AlterUniqueTogether(
            name='useranswermultiple',
            unique_together={('user', 'question')},
        ),
    ]
