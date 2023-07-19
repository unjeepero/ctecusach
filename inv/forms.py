from django import forms
from datetime import datetime

from .models import Categoria, SubCategoria, Marca, \
    UnidadMedida, Producto


class CategoriaForm(forms.ModelForm):
    class Meta:
        model=Categoria
        fields = ['descripcion','estado']
        labels = {'descripcion':"Descripción de la Categoría",
               "estado":"Estado"}
        widget={'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

class SubCategoriaForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.filter(estado=True)
        .order_by('descripcion')
    )
    class Meta:
        model=SubCategoria
        fields = ['categoria','descripcion','estado']
        labels = {'descripcion':"Sub Categoría",
               "estado":"Estado"}
        widget={'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
        self.fields['categoria'].empty_label =  "Seleccione Categoría"


class MarcaForm(forms.ModelForm):
    class Meta:
        model=Marca
        fields = ['descripcion','estado']
        labels= {'descripcion': "Descripción de la Marca",
                "estado":"Estado"}
        widget={'descripcion': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class UMForm(forms.ModelForm):
    class Meta:
        model=UnidadMedida
        fields = ['descripcion','estado']
        labels= {'descripcion': "Descripción de la Marca",
                "estado":"Estado"}
        widget={'descripcion': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


# VARIABLE DE FECHA
anio = datetime.today().strftime('%Y')
mes = datetime.today().strftime('%m')
dia = datetime.today().strftime('%d')
date_now = '{}-{}-{}'.format(anio, mes, dia )

class ProductoForm(forms.ModelForm):
#    ultimma_compra = DateField(widget=TextInput({'value' : date_now, 'type': 'date'}) )    

    class Meta:
        model=Producto
        fields='__all__'
#        fields=['codigo','codigo_barra','descripcion','precio','ultima_compra',
#                'marca','unidad_medida','subcategoria','foto','zona', 'espesor',
#                'densidad','coeficiente_conductividad','vigencia_inscripcion',
#                'usos','glosa','moneda','consumo','clase_energetica','potencia',
#                'eficiencia_energetica','url_ult_precio','precio_constructora',
#                'nombre_comercial','resistencia_termica','transmitacia_termica',
#                'huella_carbono','estado']
        exclude = ['um','fm','uc','fc','existencia']
        widget={'descripcion': forms.TextInput(),
                'ultima_compra': forms.DateInput(
                format='%Y-%m-%d',
                attrs = {
                    'type': 'date',
                    'class': 'input-group-field'}
                )
                }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        #self.fields['ultima_compra'].widget.attrs['readonly'] = True
        #self.fields['existencia'].widget.attrs['readonly'] = True



