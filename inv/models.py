from model_utils.models import TimeStampedModel

from django.db import models

from bases.models import ClaseModelo

class Categoria(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la Categoría',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Categoria, self).save()

    class Meta:
        verbose_name_plural= "Categorias"


class SubCategoria(ClaseModelo):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la Categoría'
    )

    def __str__(self):
        return '{}:{}'.format(self.categoria.descripcion,self.descripcion)
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(SubCategoria, self).save()

    class Meta:
        verbose_name_plural= "Sub Categorias"
        unique_together = ('categoria','descripcion')


class Marca(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la Marca',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Marca, self).save()

    class Meta:
        verbose_name_plural = "Marca"


class UnidadMedida(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la Unidad Medida',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(UnidadMedida, self).save()

    class Meta:
        verbose_name_plural = "Unidades de Medida"


class Producto(ClaseModelo):
    ZONA0= 'Seleccione..'
    ZONA1= 'Zona 1'
    ZONA2= 'Zona 2'
    ZONA3= 'Zona 3'
    ZONA4= 'Zona 4'
    ZONA5= 'Zona 5'
    ZONA6= 'Zona 6'
    ZONA7= 'Zona 7'
    ZONA7= 'Todas'

    ZONA_GEOGRAFICA = [
        (ZONA0, 'Seleccione..'),
        (ZONA1, 'Zona 1'),
        (ZONA2, 'Zona 2'),
        (ZONA3, 'Zona 3'),
        (ZONA4, 'Zona 4'),
        (ZONA5, 'Zona 5'),
        (ZONA6, 'Zona 6'),
        (ZONA7, 'Zona 7'),
        (ZONA7, 'Todas')
    ]

    ET0= 'Etiquetado..'
    ET1= 'A+++'
    ET2= 'A++'
    ET3= 'A+'
    ET4= 'A'
    ET5= 'B'
    ET6= 'C'
    ET7= 'D'
    ET8= 'E'
    ET9= 'F'
    ET10= 'G'
    ET11= 'Energy Start'
    ET12= 'No Informa'
    ETIQUETADO = [
        (ET0, 'Etiquetado..'),
        (ET1, 'A+++'),
        (ET2, 'A++'),
        (ET3, 'A+'),
        (ET4, 'A'),
        (ET5, 'B'),
        (ET6, 'C'),
        (ET7, 'D'),
        (ET8, 'E'),
        (ET9, 'F'),
        (ET10, 'G'),
        (ET11, 'Energy start'),
        (ET12, 'No Informa')
    ]

    M0= 'Moneda..'
    M1= 'CLP'
    M2= 'USD'
    M3= 'YEN'
    M4= 'EU'
    M5= 'OTR'
    MONEDA = [
        (M0, 'Seleccione..'),
        (M1, 'CLP'),
        (M2, 'USD'),
        (M3, 'YEN'),
        (M4, 'EU'),
        (M5, 'OTR')
    ]    
    codigo = models.CharField(
        max_length=20,
        unique=True
    )
    codigo_barra = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    precio = models.FloatField(default=0)
    existencia = models.IntegerField(default=0)
    ultima_compra = models.DateField(null=True, blank=True)

    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    unidad_medida = models.ForeignKey(UnidadMedida, on_delete=models.CASCADE)
    subcategoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to="images/",null=True,blank=True)

    zona = models.CharField(max_length=20, choices=ZONA_GEOGRAFICA, default=ZONA0)
    espesor = models.CharField(max_length=50, blank=True, null=True)
    densidad = models.CharField(max_length=50, blank=True, null=True)
    coeficiente_conductividad = models.CharField(max_length=50, blank=True, null=True)
    vigencia_inscripcion = models.CharField(max_length=50, blank=True, null=True)
    usos = models.TextField(max_length=200, blank=True, null=True)
    glosa = models.TextField(blank=True,null=True)
    moneda = models.CharField(max_length=20, choices=MONEDA, default=ZONA0)
    consumo = models.CharField(max_length=50, blank=True, null=True)
    clase_energetica = models.CharField(max_length=20, choices=ETIQUETADO, default=ZONA0)
    potencia =  models.CharField(max_length=50, blank=True, null=True)
    eficiencia_energetica = models.CharField(max_length=50, blank=True, null=True)
    url_ult_precio = models.CharField(max_length=50, blank=True, null=True)
    precio_constructora = models.FloatField(default=0)
    nombre_comercial = models.CharField(max_length=200, blank=True, null=True)
    resistencia_termica = models.CharField(max_length=50, blank=True, null=True)
    transmitacia_termica = models.CharField(max_length=50, blank=True, null=True)
    huella_carbono = models.CharField(max_length=100, blank=True, null=True)

    zona2 = models.CharField(max_length=20, choices=ZONA_GEOGRAFICA, default=ZONA0)
    espesor2 = models.CharField(max_length=50, blank=True, null=True)
    densidad2 = models.CharField(max_length=50, blank=True, null=True)
    coeficiente_conductividad2 = models.CharField(max_length=50, blank=True, null=True)
    vigencia_inscripcion2 = models.CharField(max_length=50, blank=True, null=True)
    resistencia_termica2 = models.CharField(max_length=50, blank=True, null=True)
    transmitacia_termica2 = models.CharField(max_length=50, blank=True, null=True)

    zona3 = models.CharField(max_length=20, choices=ZONA_GEOGRAFICA, default=ZONA0)
    espesor3 = models.CharField(max_length=50, blank=True, null=True)
    densidad3 = models.CharField(max_length=50, blank=True, null=True)
    coeficiente_conductividad3 = models.CharField(max_length=50, blank=True, null=True)
    vigencia_inscripcion3 = models.CharField(max_length=50, blank=True, null=True)
    resistencia_termica3 = models.CharField(max_length=50, blank=True, null=True)
    transmitacia_termica3 = models.CharField(max_length=50, blank=True, null=True)

    zona4 = models.CharField(max_length=20, choices=ZONA_GEOGRAFICA, default=ZONA0)
    espesor4 = models.CharField(max_length=50, blank=True, null=True)
    densidad4 = models.CharField(max_length=50, blank=True, null=True)
    coeficiente_conductividad4 = models.CharField(max_length=50, blank=True, null=True)
    vigencia_inscripcion4 = models.CharField(max_length=50, blank=True, null=True)
    resistencia_termica4 = models.CharField(max_length=50, blank=True, null=True)
    transmitacia_termica4 = models.CharField(max_length=50, blank=True, null=True)

    zona5 = models.CharField(max_length=20, choices=ZONA_GEOGRAFICA, default=ZONA0)
    espesor5 = models.CharField(max_length=50, blank=True, null=True)
    densidad5 = models.CharField(max_length=50, blank=True, null=True)
    coeficiente_conductividad5 = models.CharField(max_length=50, blank=True, null=True)
    vigencia_inscripcion5 = models.CharField(max_length=50, blank=True, null=True)
    resistencia_termica5 = models.CharField(max_length=50, blank=True, null=True)
    transmitacia_termica5 = models.CharField(max_length=50, blank=True, null=True)

    zona6 = models.CharField(max_length=20, choices=ZONA_GEOGRAFICA, default=ZONA0)
    espesor6 = models.CharField(max_length=50, blank=True, null=True)
    densidad6 = models.CharField(max_length=50, blank=True, null=True)
    coeficiente_conductividad6 = models.CharField(max_length=50, blank=True, null=True)
    vigencia_inscripcion6 = models.CharField(max_length=50, blank=True, null=True)
    resistencia_termica6 = models.CharField(max_length=50, blank=True, null=True)
    transmitacia_termica6 = models.CharField(max_length=50, blank=True, null=True)

    zona7 = models.CharField(max_length=20, choices=ZONA_GEOGRAFICA, default=ZONA0)
    espesor7 = models.CharField(max_length=50, blank=True, null=True)
    densidad7 = models.CharField(max_length=50, blank=True, null=True)
    coeficiente_conductividad7 = models.CharField(max_length=50, blank=True, null=True)
    vigencia_inscripcion7 = models.CharField(max_length=50, blank=True, null=True)
    resistencia_termica7 = models.CharField(max_length=50, blank=True, null=True)
    transmitacia_termica7 = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.descripcion)
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Producto,self).save()
    
    class Meta:
        verbose_name_plural = "Productos"
#        unique_together = ('codigo','codigo_barra')