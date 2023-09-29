from django.db import models


class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    contato = models.CharField(max_length=100)
    endereco = models.TextField()

    def __str__(self):
        return self.nome
    

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    qualificacoes = models.TextField()
    contato = models.CharField(max_length=100)
    horario_disponivel = models.TextField()

    def __str__(self):
        return self.nome
    
class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome
    


class Serie(models.Model):
    nome = models.CharField(max_length=100)
    ano_letivo = models.IntegerField()

    def __str__(self):
        return self.nome
    
class AnoLetivo(models.Model):
    ano = models.PositiveIntegerField(unique=True)
    inicio = models.DateField()
    fim = models.DateField()

    def __str__(self):
        return f"Ano Letivo {self.ano}"

    class Meta:
        ordering = ['-ano']
    
class Matricula(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE)
    ano_letivo = models.ForeignKey(AnoLetivo, on_delete=models.CASCADE)
    data_matricula = models.DateField(auto_now_add=True)
    matricula = models.CharField(max_length=20, unique=True, blank=True)
    ativa = models.BooleanField(True)

    class Meta:
        unique_together = ('aluno', 'serie', 'ano_letivo')

    def __str__(self):
        return f"Matrícula de {self.aluno} na {self.serie} ({self.ano_letivo})"
    
    def gerar_matricula(cls, aluno, serie, ano_letivo):
        codigo_aluno = aluno.id 
        matricula = f"{ano_letivo}{serie.id:02d}{codigo_aluno:04d}"
        return matricula
    
    def save(self, *args, **kwargs):
        if not self.matricula:
            self.matricula = self.gerar_matricula(self.aluno, self.serie, self.ano_letivo)




class Aula(models.Model):
    data = models.DateField()
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    alunos = models.ManyToManyField(Aluno, blank=True)

    def __str__(self):
        return f"Aula de {self.disciplina} na {self.serie} - {self.data} ({self.hora_inicio}-{self.hora_fim})"

