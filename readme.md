## Introdução

Este é o repositório de um modelo de classificação textual que tem como objetivo identificar a dificuldade de um texto em português de acordo com as categorias: ensino fundamental I, ensino fundamental II, ensino médio e ensino superior. O projeto foi desenvolvido em Python, utilizando a biblioteca Scikit-Learn para a construção do modelo e o framework Flask para a criação da aplicação web. 

Após desenvolvimento, os aquivos necessários para a execução do modelo foram salvos no diretório `web_app/model`.

A metodologia de desenvolvimeto é apresentada no arquivo `Relatório___Processo_Seletivo___Estágio___CAED.pdf`, e mais detalhes podem ser encontrados no notebook `text-complexity.ipynb`.

## Como executar

- Criar um virtualenv: `python -m venv venv`
- Instalar as dependências do projeto: `pip install -r requirements.txt`
- Executar a aplicação: `flask --app web_app/app.py run` 
- Acessar a aplicação no navegador pelo endereço apresentado no terminal