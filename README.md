# Mateus Erkmann - D3 Covid Predict
Predict de casos de covid em X dias futuros

[Exemplo rodando do projeto](http://hpx08.pythonanywhere.com/api/v1/predict/4/)

URL padrão para predição: `/api/v1/predict/:numeroDeDias/`

Collection para importação no **Postman**, com URL da aplicação rodando, está no arquivo `CovidMateusErkmann.postman_collection.json`

## O Projeto
O sistema deve receber um numero N de dias, e devolver uma previsão de novos casos de COVID-19 para cada um dos dias em N dias

### Método
Dado o [CSV](https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/jhu/new_cases.csv) de fonte de dados (atualizado diariamente), o sistema pega os casos de COVID,
por dia, dos últimos N dias, faz a média aritmética dos casos, e projeta para o primeiro dia, depois refaz a lista de dias base, utilizando os casos previstos,
 para refazer a média, e projetar ao dia seguinte, sempre utilizando N dias atrás (ou o total de dias disponíveis) como parâmetro para a média. Assim faz sucessivamente
 N vezes, e retorna cada dia e seu respectivo valor previsto de casos.

## Instalação
### Requer:
- Python>=3.8
- criar e ativar venv -> `python3 -m venv venv` -> `source venv/bin/activate`
- no diretorio `d3-covid` (raiz do projeto) instalar os requirements -> `pip install -r requirements.txt`

## Execução (venv ativada)
- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py runserver`


Aplicação estará rodando em `localhost:8000`

## Testes (venv ativada)
- `python manage.py test`
