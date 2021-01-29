# Generated by Django 3.0.7 on 2021-01-18 19:54

from django.db import migrations, models

def empty_to_null(apps, schema_editor):
    User = apps.get_model("bookwyrm", "User")
    db_alias = schema_editor.connection.alias
    User.objects.using(db_alias).filter(email="").update(email=None)

def null_to_empty(apps, schema_editor):
    User = apps.get_model("bookwyrm", "User")
    db_alias = schema_editor.connection.alias
    User.objects.using(db_alias).filter(email=None).update(email="")

class Migration(migrations.Migration):

    dependencies = [
        ('bookwyrm', '0036_annualgoal'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shelfbook',
            options={'ordering': ('-created_date',)},
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.RunPython(empty_to_null, null_to_empty),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
    ]