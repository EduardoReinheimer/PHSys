from django.db import models

class Etapa(models.Model):
     descricao = models.CharField(max_length=255)
     tempo = models.TimeField(auto_now=False)
    #  STATUS_ETAPA = [
    #      ('AB', 'ABERTO'),
    #      ('EE','EM EXECUCAO'),
    #      ('PR', 'PRONTO')
    #  ]
    #  status = models.CharField(
    #      max_length=2,
    #      choices=STATUS_ETAPA,
    #      default='AB'
    #  )
    
class Marca(models.Model):
    nome = models.CharField(max_length=120)
    autorizada = models.BooleanField()
    def __str__(self):
        return self.nome
    
class Veiculo(models.Model):
    modelo = models.CharField(max_length=120)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    SUV = 'SV'
    PICAPE = 'PK'
    AUTOMOVEL = 'AT'
    VAN = 'VN'
    CATEGORIA_VEICULO = [
        (SUV, 'SUV'),
        (PICAPE, 'PICAPE'),
        (AUTOMOVEL, 'AUTOMOVEL'),
        (VAN, 'VAN')
    ]
    categoria = models.CharField(
        max_length=2,
        choices=CATEGORIA_VEICULO,
        default=AUTOMOVEL
    )
    def __str__(self) :
        return f'{self.marca} - {self.modelo}'
     
