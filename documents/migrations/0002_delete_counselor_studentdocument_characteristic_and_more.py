# Generated by Django 4.1.3 on 2022-11-26 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
        ('documents', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Counselor',
        ),
        migrations.AddField(
            model_name='studentdocument',
            name='characteristic',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='studentdocument',
            name='counselors_inn',
            field=models.CharField(max_length=15, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='studentdocument',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='studentdocument',
            name='grade',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='studentdocument',
            name='guardians_inn',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='studentdocument',
            name='guardians_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='studentdocument',
            name='guardians_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='studentdocument',
            name='guardians_surname',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='studentdocument',
            name='image',
            field=models.ImageField(null=True, upload_to='students_image'),
        ),
        migrations.AddField(
            model_name='studentdocument',
            name='middle_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='studentdocument',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='studentdocument',
            name='nation',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='studentdocument',
            name='school_name',
            field=models.CharField(choices=[('1', 'Аламединская 1'), ('38', '38 Гимназия'), ('Айчурок', 'Айчурок'), ('61', '61 школа'), ('67', '67 школа гимназия')], max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='studentdocument',
            name='student_class',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='studentdocument',
            name='students_inn',
            field=models.CharField(max_length=15, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='studentdocument',
            name='subject',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='studentdocument',
            name='surname',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='studentdocument',
            name='users_inn',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='school.students'),
        ),
    ]
