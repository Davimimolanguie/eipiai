from random import choice
from flask import Flask, request 
b = 9
oprint = ""
dezeroanove = "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
print("olá,bem vindo(a) ao gerador de cpf")
app = Flask(__name__)
@app.route('/gerar-cpf', methods=['GET'])
def gerar_cpfs():
    quantidade = request.args.get('quantidade')
    print(quantidade)
    if quantidade and quantidade.isdigit():
        quantoscpf = int(quantidade) 
        return gerar_cpfs_lista(quantoscpf)
    else:
        return "Por favor, forneça um número válido para a quantidade (ex: ?quantidade=3)"
def gerar_cpfs_lista(quantoscpf):
    cpfs_gerados = []
    for _ in range(quantoscpf):
        cpf = ''.join(choice(dezeroanove) for _ in range(11)) 
        cpfs_gerados.append(cpf)
    return "<br>".join(cpfs_gerados)
if __name__ == '__main__':
    app.run(debug=True)