# Generated by Django 4.0.4 on 2022-05-31 03:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manageFiles', '0002_file_division_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='JGDepartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DepartmentName', models.CharField(blank=True, max_length=200, null=True)),
                ('NothiCode', models.CharField(blank=True, max_length=3, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='JGDivision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DivisionName', models.CharField(blank=True, max_length=200, null=True)),
                ('NothiCode', models.CharField(blank=True, max_length=3, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='JGSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SectionName', models.CharField(blank=True, max_length=200, null=True)),
                ('NothiCode', models.CharField(blank=True, max_length=3, null=True)),
                ('JGDepartment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manageFiles.jgdepartment')),
            ],
        ),
        migrations.RemoveField(
            model_name='file',
            name='division_name',
        ),
        migrations.AlterField(
            model_name='file',
            name='file_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='file',
            name='file_number',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.CreateModel(
            name='JGSubSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SubSectionName', models.CharField(blank=True, max_length=200, null=True)),
                ('NothiCode', models.CharField(blank=True, max_length=3, null=True)),
                ('JGSection', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manageFiles.jgsection')),
            ],
        ),
        migrations.AddField(
            model_name='jgdepartment',
            name='JGDivision',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manageFiles.jgdivision'),
        ),
        migrations.AddField(
            model_name='file',
            name='file_department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manageFiles.jgdepartment'),
        ),
        migrations.AddField(
            model_name='file',
            name='file_division',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manageFiles.jgdivision'),
        ),
        migrations.AddField(
            model_name='file',
            name='file_section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manageFiles.jgsection'),
        ),
    ]
