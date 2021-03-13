#ter o mesmo nome definido no atributo name, em 
# experiencein/usuarios/templates/registrar.html
from django import forms
#usuário já existir no banco
from django.contrib.auth.models import User

class RegistrarUsuarioForm(forms.Form):

    nome = forms.CharField(required=True), 
    email = forms.EmailField(required=True)
    senha = forms.CharField(required=True)
    telefone = forms.CharField(required=True)
    nome_empresa = forms.CharField(required=True)

    #Validando os dados do formulário
    def is_valid(self):
        valid = True
        if not super(RegistrarUsuarioForm, self).is_valid():
            self.adiciona_erro('Por favor, verifique os dados informados')
            valid = False

        user_exists = User.objects.filter(username=self.data['nome']).exists()

        if user_exists:
            self.adiciona_erro('Usuario ja existente')
            valid = False

        return valid

    #função para adicionar a mensagem de erro
    def adiciona_erro(self, message):
        errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        errors.append(message)