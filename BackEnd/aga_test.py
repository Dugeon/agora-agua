import os
import requests
from agabackend import criar_usuario, exibir_usuario, usuario_existente, salvar_usuario, ler_usuarios


# Teste 1: Verificar criação de usuário duplicado
def test_usuario_duplicado():
  
    usuario = {'nome': 'Fulano', 'telefone': '123456789', 'cep': '12345-678', 'email': 'fulano@example.com'}
  
    assert usuario_existente(usuario) == True


# Teste 2: Testar cadastro de novo usuário via rota
def test_cadastrar_usuario_via_rota():
  
    dados = {'nome': 'Teste', 'telefone': '999999999', 'cep': '00000-000', 'email': 'teste@example.com'}
    response = requests.post('http://localhost:5000/BackEnd/cadastro', json=dados)
   
    assert response.status_code == 200


# Teste 3: Testar listagem de usuários
def test_listar_usuarios():
  
    response = requests.get('http://localhost:5000/BackEnd/usuarios')
   
    assert response.status_code == 200
   
    assert len(response.json()) > 0


# Teste 4: Testar busca de usuário específico
def test_buscar_usuario():
    email = 'fulano@example.com'
    response = requests.get(f'http://localhost:5000/BackEnd/usuarios?email={email}')
    
    #print(response.json())

    assert response.status_code == 200
    
    assert isinstance(response.json(), list)

    assert any(user.get('email') == email for user in response.json())


# Teste 5: Testar formatação de dados de usuário
def test_formatar_dados_usuario():
   
    usuario = {'nome': 'Teste', 'telefone': '999999999', 'cep': '00000-000', 'email': 'teste@example.com'}
    resultado_esperado = "Dados do usuário:\nNome: Teste\nTelefone: 999999999\nCEP: 00000-000\nE-mail: teste@example.com"
   
    assert exibir_usuario(usuario) == resultado_esperado


# Teste 6: Verificar existência do arquivo CSV
def test_existencia_arquivo_csv():
   
    assert os.path.isfile('usuarios.csv')


# Teste 7: Testar leitura do arquivo CSV
def test_leitura_arquivo_csv():
   
    usuarios = ler_usuarios()
   
    assert len(usuarios) > 0


# Teste 8: Testar verificação de usuário existente
def test_verificar_usuario_existente():
   
    usuario = {'nome': 'Fulano', 'telefone': '123456789', 'cep': '12345-678', 'email': 'fulano@example.com'}
   
    assert usuario_existente(usuario) == True


# Teste 9: Testar salvar usuário no CSV
def test_salvar_usuario_csv():
   
    usuario = {'nome': 'Teste', 'telefone': '999999999', 'cep': '00000-000', 'email': 'teste@example.com'}
    salvar_usuario(usuario)
    usuarios = ler_usuarios()
   
    assert usuario in usuarios


# Teste 10: Testar integridade dos dados salvos no CSV
def test_integridade_dados_csv():
   
    usuarios = ler_usuarios()
   
    for usuario in usuarios:
        assert 'nome' in usuario
        assert 'telefone' in usuario
        assert 'cep' in usuario
        assert 'email' in usuario