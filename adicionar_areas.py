import os
import django

# Definindo as configurações do Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "seu_projeto.settings")
django.setup()

from area_interesse.models import AreaInteresse

areas = [
    'Teste de software', 'Redes de Computadores', 'Agricultura Digital',
    'Algoritmos', 'Análise e Projeto de Sistemas', 'Aprendizado de Máquina',
    'Avaliação de Desempenho de Sistemas', 'Banco de Dados', 'Desenvolvimento para Dispositivos Móveis',
    'Desenvolvimento Multiplataforma', 'Desenvolvimento Web', 'DevOps', 'E-Learning',
    'Engenharia de Software', 'Estatística', 'Estrutura de Dados', 'Gestão de Tecnologia da Informação',
    'Inclusão Digital'
]

for nome in areas:
    if not AreaInteresse.objects.filter(nome=nome).exists():  # Verifica se já existe
        AreaInteresse.objects.create(nome=nome)
    else:
        print(f"A área '{nome}' já existe.")
