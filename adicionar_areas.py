import requests

# Lista das áreas de interesse
areas_de_interesse = [
    "Teste de software",
    "Redes de Computadores",
    "Agricultura Digital",
    "Algoritmos",
    "Análise e Projeto de Sistemas",
    "Aprendizado de Máquina",
    "Avaliação de Desempenho de Sistemas",
    "Banco de Dados",
    "Desenvolvimento para Dispositivos Móveis",
    "Desenvolvimento Multiplataforma",
    "Desenvolvimento Web",
    "DevOps",
    "E-Learning",
    "Engenharia de Software",
    "Estatística",
    "Estrutura de Dados",
    "Gestão de Tecnologia da Informação",
    "Inclusão Digital",
    # Você pode adicionar mais áreas aqui conforme necessário
]

# URL do endpoint
url = "https://backend-sigoo.render.com/api/area-interesse/add/"

# Função para enviar o POST para o backend
def adicionar_area_de_interesse(nome):
    # Corpo da requisição com o nome da área de interesse
    body = {"nome": nome}
    
    # Enviando a requisição POST
    response = requests.post(url, json=body)
    
    # Verificando se a requisição foi bem-sucedida
    if response.status_code == 200:
        print(f"Área de interesse '{nome}' adicionada com sucesso!")
    else:
        print(f"Erro ao adicionar a área de interesse '{nome}'. Status Code: {response.status_code}")

# Loop para adicionar todas as áreas de interesse
for area in areas_de_interesse:
    adicionar_area_de_interesse(area)
