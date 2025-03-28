from flask import Flask, jsonify
import random
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

charadas = [
    {'id':1, 'pergunta':'O que é, o que é? Quando você tem, quer compartilhar, mas quando você compartilha, não tem mais.', 'reposta':'Um segredo!' },
    {'id':2, 'pergunta':'Qual animal tem quatro patas pela manhã, duas pela tarde e três patas à noite?', 'reposta':'O ser humano' },
    {'id':3, 'pergunta':' Oque é que todo mundo tem,más ninguém pode perder?', 'reposta':'A sombra' },
    {'id':4, 'pergunta':'Qual é o instrumento que não pode ser visto, não pode ser tocado, mas pode ser ouvido?', 'reposta':'A voz' },
    {'id':5, 'pergunta':'Por que o computador foi preso?', 'reposta':'Porque ele executou um programa' },
    {'id':6, 'pergunta':'Eu tenho uma enxada, uma pá e uma foice. Quantas ferramentas eu tenho?', 'reposta':'Duas, porque uma foi-se.' },
    {'id':7, 'pergunta':' O que um cientista careca disse para um outro cientista careca?', 'reposta':'Lisossomos.' },
    {'id':8, 'pergunta':' O que o zero disse para o oito?', 'reposta':'Que cinto maneiro! 0 💞 8' },
    {'id':9, 'pergunta':' O que um cientista careca disse para um outro cientista careca?', 'reposta':'Lisossomos.' },
    {'id':10, 'pergunta':' O que é, o que é? Uma impressora disse para a outra.', 'reposta':'Essa folha é sua ou é impressão minha?' },
]

@app.route('/')
def index():
    return 'API ADA TA ON. ria '

@app.route('/charadas', methods=['GET'])
def lista():
    return jsonify(random.choice(charadas)), 200

@app.route('/charadas/<campo>/<busca>', methods=['GET'])
def busca(campo, busca):

    if campo not in ['id','pergunta','reposta']:
        return jsonify({'mensagem': 'ERRO! Campo não encontrado'})
    if campo == 'id':
            busca = int(busca)

    for charada in charadas:
        if charada [campo] == busca:
            return jsonify(charada), 200
    else:
        return jsonify({'mensagem': 'ERRO! Charada não encontrado'}), 404 

# @app.route ('/todascharadas', methods=['GET'])
# def lista():
#     return jsonify(charadas), 200


if __name__ == '__main__':
    app.run(debug=True)