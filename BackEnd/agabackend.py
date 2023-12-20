from flask import Flask, request, jsonify
import csv
import os


app = Flask(__name__)


def verificar_csv_existente():
    
    if not os.path.isfile('usuarios.csv'):
    
        with open('usuarios.csv', mode='w', newline='') as file:
    
            fieldnames = ['nome', 'telefone', 'cep', 'email']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            exemplos_usuarios = [
                {'nome': 'Fulano', 'telefone': '123456789', 'cep': '12345-678', 'email': 'fulano@example.com'},
                {'nome': 'Ciclano', 'telefone': '987654321', 'cep': '98765-432', 'email': 'ciclano@example.com'},
                {'nome': 'Fulano', 'telefone': '123456789', 'cep': '12345-678', 'email': 'fulano@example.com'},
                {'nome': 'Ciclano', 'telefone': '987654321', 'cep': '98765-432', 'email': 'ciclano@example.com'},
                {'nome': 'Beltrano', 'telefone': '555555555', 'cep': '54321-000', 'email': 'beltrano@example.com'},
                {'nome': 'Maria', 'telefone': '987654321', 'cep': '34567-890', 'email': 'maria@example.com'},
                {'nome': 'João', 'telefone': '333333333', 'cep': '22222-111', 'email': 'joao@example.com'},
                {'nome': 'Ana', 'telefone': '444444444', 'cep': '12345-543', 'email': 'ana@example.com'},
                {'nome': 'José', 'telefone': '666666666', 'cep': '98765-123', 'email': 'jose@example.com'},
                {'nome': 'Carlos', 'telefone': '777777777', 'cep': '87654-321', 'email': 'carlos@example.com'},
                {'nome': 'Julia', 'telefone': '888888888', 'cep': '76543-210', 'email': 'julia@example.com'},
                {'nome': 'Roberto', 'telefone': '999999999', 'cep': '65432-109', 'email': 'roberto@example.com'},
                {'nome': 'Mariana', 'telefone': '101010101', 'cep': '54321-980', 'email': 'mariana@example.com'},
                {'nome': 'Lúcia', 'telefone': '111111111', 'cep': '11111-111', 'email': 'lucia@example.com'},
                {'nome': 'Rafael', 'telefone': '121212121', 'cep': '22222-222', 'email': 'rafael@example.com'},
                {'nome': 'Aline', 'telefone': '131313131', 'cep': '33333-333', 'email': 'aline@example.com'},
                {'nome': 'Pedro', 'telefone': '141414141', 'cep': '44444-444', 'email': 'pedro@example.com'},
                {'nome': 'Beatriz', 'telefone': '151515151', 'cep': '55555-555', 'email': 'beatriz@example.com'},
                {'nome': 'Gustavo', 'telefone': '161616161', 'cep': '66666-666', 'email': 'gustavo@example.com'},
                {'nome': 'Fernanda', 'telefone': '171717171', 'cep': '77777-777', 'email': 'fernanda@example.com'},
                {'nome': 'Camila', 'telefone': '181818181', 'cep': '88888-888', 'email': 'camila@example.com'},
                {'nome': 'Lucas', 'telefone': '191919191', 'cep': '99999-999', 'email': 'lucas@example.com'},
                {'nome': 'Carolina', 'telefone': '202020202', 'cep': '10101-010', 'email': 'carolina@example.com'},
                {'nome': 'Diego', 'telefone': '212121212', 'cep': '20202-020', 'email': 'diego@example.com'},
                {'nome': 'Luana', 'telefone': '232323232', 'cep': '30303-030', 'email': 'luana@example.com'},
                {'nome': 'Roberta', 'telefone': '242424242', 'cep': '40404-040', 'email': 'roberta@example.com'},
                {'nome': 'Vitor', 'telefone': '252525252', 'cep': '50505-050', 'email': 'vitor@example.com'},
                {'nome': 'Fernando', 'telefone': '262626262', 'cep': '60606-060', 'email': 'fernando@example.com'},
                {'nome': 'Laura', 'telefone': '272727272', 'cep': '70707-070', 'email': 'laura@example.com'},
                {'nome': 'Isabela', 'telefone': '282828282', 'cep': '80808-080', 'email': 'isabela@example.com'},
                {'nome': 'Miguel', 'telefone': '292929292', 'cep': '90909-090', 'email': 'miguel@example.com'},
                {'nome': 'Larissa', 'telefone': '303030303', 'cep': '01010-101', 'email': 'larissa@example.com'}
            ]

            for usuario in exemplos_usuarios:

                writer.writerow(usuario)


# Função para criar um novo usuário e salvar no CSV
def criar_usuario(nome, telefone, cep, email):

    usuario = {'nome': nome, 'telefone': telefone, 'cep': cep, 'email': email}
    salvar_usuario(usuario)
    return usuario


# Função para ler todos os usuários do CSV
def ler_usuarios():
   
    with open('usuarios.csv', mode='r', newline='') as file:
       
        reader = csv.DictReader(file)
        usuarios = [{key: value.strip() for key, value in linha.items()} for linha in reader]

    return usuarios


# Função para exibir um usuário
def exibir_usuario(usuario):

    return f"Dados do usuário:\nNome: {usuario['nome']}\nTelefone: {usuario['telefone']}\nCEP: {usuario['cep']}\nE-mail: {usuario['email']}"

# Função para verificar se um usuário já está cadastrado com os mesmos dados
def usuario_existente(usuario):

    with open('usuarios.csv', mode='r', newline='') as file:
        
        reader = csv.DictReader(file)
        
        for linha in reader:
        
            if (
        
                linha['email'] == usuario['email']
                and linha['nome'] == usuario['nome']
                and linha['telefone'] == usuario['telefone']
                and linha['cep'] == usuario['cep']
        
            ):
        
                return True
    
    return False


# Função para salvar um usuário no CSV
def salvar_usuario(usuario):

    if usuario_existente(usuario):

        print("Usuário já cadastrado com os mesmos dados e e-mail.")

    else:

        with open('usuarios.csv', mode='a', newline='') as file:

            fieldnames = ['nome', 'telefone', 'cep', 'email']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            if file.tell() == 0:

                writer.writeheader()

            writer.writerow(usuario)


# Rota para cadastrar um novo usuário
@app.route('/BackEnd/cadastro', methods=['POST'])

def cadastrar_usuario():

    data = request.json
    novo_usuario = criar_usuario(data['nome'], data['telefone'], data['cep'], data['email'])

    return jsonify({'message': 'Dados cadastrados com sucesso!'}), 200


# Rota para obter todos os usuários
@app.route('/BackEnd/usuarios', methods=['GET'])

def get_usuarios():
    
    usuarios = ler_usuarios()
    return usuarios

if __name__ == '__main__':

    verificar_csv_existente()

    app.run(debug=True)
