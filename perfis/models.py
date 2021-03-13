from django.db import models

#Importar user
from django.contrib.auth.models import User
# Create your models here.
# Estrutura do banco de dados

# Foi criado uma tabela chamada Perfil
class Perfil(models.Model):

	nome = models.CharField(max_length=255, null=False)
	#retirar email pois será validado pelo Django
	telefone = models.CharField(max_length=15, null=False)
	nome_empresa = models.CharField(max_length=255, null=False)
	# novidade aqui. Novo atributo!
	contatos = models.ManyToManyField('self')

	#relacionamento um para um entre nossa classe Perfil e a classe User
	usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name="perfil")

	#delegar acesso para a classe User - email
	@property
	def email(self):
		return self.usuario.email

	def convidar(self, perfil_convidado):
		Convite(solicitante=self, convidado=perfil_convidado).save()

class Convite(models.Model):
	solicitante = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='convites_feitos')
	convidado = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='convites_recebidos')
	#tabala Convite, com id do solicitante e convidado(chave estrangeira).
	# Relação 1 x 1
	def aceitar(self):
		self.convidado.contatos.add(self.solicitante)
		self.solicitante.contatos.add(self.convidado)
		self.delete()