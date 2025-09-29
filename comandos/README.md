python -m venv venv
. venv/bin/activate (MAC/Linux)
.\venv\Scripts\activate (Windows)
python -m pip install django
django-admin startproject project .
python manage.py startapp contact

# Configurar o git

git config --global user.name 'Seu nome'
git config --global user.email 'seu_email@gmail.com'
git config --global init.defaultBranch main

# Configure o .gitignore
git init
git add .
git commit -m 'Mensagem'
git remote add origin URL_DO_GIT

# Migrando a base de dados do Django

python manage.py makemigrations
python manage.py migrate

# Criando e modificando a senha de um super usuário Django

python manage.py createsuperuser
python manage.py changepassword USERNAME

# Trabalhando com o model do Django

# Importa o módulo
from contact.models import Contact
# Cria um contato (Lazy)
# Retorna o contato
contact = Contact(**fields)
contact.save()
# Cria um contato (Não lazy)
# Retorna o contato
contact = Contact.objects.get(pk=10)
# Edita um contato
# Retorna o contato
Contact.field_name1 = 'Novo valor 1'
contact.field_name2 = 'Novo valor 2'
contact.save()
# Apaga um contato
# Depende da base de dados, geralmente retorna o número
# de valores manipulados na base de dados
contacts = Contact.objects.all().order_by('id')
# Seleciona cintatos usandi filtros
# Retorna QuerySet[]
contacts = Contact.objets.filter(**filters).order_by('-id')

# Fim (TESTE)
#