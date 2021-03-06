# Generated by Django 3.1.2 on 2020-11-17 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0004_auto_20201117_0221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comprador',
            name='comuna_comprador',
            field=models.CharField(choices=[('CE', 'Cerrillos'), ('CN', 'Cerro Navia'), ('CO', 'Conchalí'), ('EB', 'El Bosque'), ('EC', 'Estación Central'), ('HU', 'Huechuraba'), ('IN', 'Independencia'), ('LA', 'La Cisterna'), ('LF', 'La Florida'), ('LG', 'La Granja'), ('LP', 'La Pintana'), ('LR', 'La Reina'), ('LC', 'Las Condes'), ('LB', 'Lo Barnechea'), ('LE', 'Lo Espejo'), ('LP', 'Lo Prado'), ('MA', 'Macul'), ('MP', 'Maipú'), ('ÑU', 'Ñuñoa'), ('PH', 'Padre Hurtado'), ('PAC', 'Pedro Aguirre Cerda'), ('PE', 'Peñalolén'), ('PI', 'Pirque'), ('PR', 'Providencia'), ('PU', 'Pudahuel'), ('PA', 'Puente Alto'), ('QU', 'Quilicura'), ('QN', 'Quinta Normal'), ('REC', 'Recoleta'), ('REN', 'Renca'), ('SB', 'San Bernardo'), ('SJ', 'San Joaquín'), ('SJM', 'San José de Maipo'), ('SM', 'San Miguel'), ('SR', 'San Ramón'), ('SAN', 'Santiago')], max_length=3),
        ),
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.CharField(choices=[('PA', 'Pasteles'), ('T', 'Torta'), ('G', 'Galletas'), ('B', 'Bollería'), ('CH', 'Chocolates'), ('B', 'Bombones'), ('PI', 'Pizza'), ('S', 'Sandwiches'), ('F', 'Frituras'), ('CO', 'Comida Oriental')], max_length=2),
        ),
        migrations.AlterField(
            model_name='producto',
            name='descripcion_producto',
            field=models.TextField(max_length=25),
        ),
        migrations.AlterField(
            model_name='producto',
            name='id_producto',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre_producto',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='producto',
            name='unidad_medida',
            field=models.CharField(choices=[('S', 'Kilogramo'), ('M', 'Gramo'), ('S', 'Unidad'), ('M', 'Docena'), ('S', 'Trozo')], max_length=1),
        ),
    ]
