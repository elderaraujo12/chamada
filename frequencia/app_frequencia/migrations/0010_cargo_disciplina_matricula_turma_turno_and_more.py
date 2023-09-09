# Generated by Django 4.2.5 on 2023-09-09 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_frequencia', '0009_cadastro_aluno_foto_cadastro_funcionario_foto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RenameModel(
            old_name='cadastro_aluno',
            new_name='Aluno',
        ),
        migrations.RenameModel(
            old_name='Cadastro_funcionario',
            new_name='Funcionario',
        ),
        migrations.DeleteModel(
            name='Login',
        ),
    ]
