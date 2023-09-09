from django.db import models

# Create your models here.
class Cargo(models.Model):
    pass

class Turno(models.Model):
    pass

class Turma(models.Model):
    pass


class Disciplina(models.Model):
    pass


class Aluno(models.Model):
    CHOICE_SEXO = (('M', 'Masculino'), ('F', 'Feminino'))
    CHOICE_TURNO = (('M', 'Manhã'), ('T', 'Tarde'), ('N', 'Noite'))
    CHOICE_TURMA = (('1', '1-A'), ('2', '1-B'), ('3', '1-C'),('4', '2-A'), ('5', '2-B'), ('6', '2-C'),('7', '3-A'), ('8', '3-B'), ('9', '3-C'))
    nome = models.CharField(max_length=100)
    idade = models.CharField(max_length=10)
    data_de_nascimento = models.DateField()
    sexo = models.CharField(max_length=11, choices=CHOICE_SEXO, blank=True) 
    turno = models.CharField(max_length=11, choices=CHOICE_TURNO, blank=True) 
    turma = models.CharField(max_length=11, choices=CHOICE_TURMA, blank=True) 
    email = models.EmailField()
    telefone = models.CharField(max_length=11)
    foto = models.ImageField()
    
    def __str__(self):
        return self.nome
    

class Funcionario(models.Model):
    CHOICE_SEXO = (('M', 'Masculino'), ('F', 'Feminino'))
    CHOICE_TURNO = (('M', 'Manhã'), ('T', 'Tarde'), ('N', 'Noite'))
    CHOICE_DICIPLINA = (('1', 'português'), ('2', 'matematica'), ('3', 'historia'),('4', 'geografia'), ('5', 'fisica'), ('6', 'biologia'),('7', 'ed:fisica'), ('8', 'informatica'), ('9', 'ingles'))
    nome = models.CharField(max_length=100)
    idade = models.CharField(max_length=10)
    data_de_nascimento = models.DateField()
    sexo = models.CharField(max_length=11, choices=CHOICE_SEXO, blank=True) 
    turno = models.CharField(max_length=11, choices=CHOICE_TURNO, blank=True) 
    diciplina = models.CharField(max_length=11, choices=CHOICE_DICIPLINA, blank=True) 
    email = models.EmailField()
    telefone = models.CharField(max_length=11)
    foto = models.ImageField()
    
    
    def __str__(self):
        return self.nome
    

    
class Matricula(models.Model):
    pass

