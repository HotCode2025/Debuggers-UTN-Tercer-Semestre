from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("turnos", "0004_alter_turno_unique_together_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="perfilusuario",
            name="ciudad",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="perfilusuario",
            name="documento",
            field=models.CharField(blank=True, max_length=30, null=True, unique=True),
        ),
        migrations.AddField(
            model_name="perfilusuario",
            name="genero",
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name="perfilusuario",
            name="provincia",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="perfilusuario",
            name="telefono",
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name="perfilusuario",
            name="tipo_documento",
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
