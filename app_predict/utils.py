from datetime import datetime, timedelta, date
import pandas as pd
import json

from .models import Dia

# Pega os dados de todos os dias a partir do dia 22/01/2020
def get_new_cases_total():
    # Le o csv com esses dados atualizados todos os dias pela OWID (somente novos casos mundiais e a data)
    return json.loads(
        pd.read_csv(
            "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/jhu/new_cases.csv",
            usecols=["date", "World"],
        ).to_json(orient="records")
    )  # converte para JSON


# Retorna o dia de ontem
def get_yesterday():
    return datetime.today() - timedelta(days=1)


# Verifica se tem o registro de casos de ontem
def check_yesterday():
    if Dia.objects.filter(data=get_yesterday()).first():
        return True
    return False


# Popula caso necessario, com os dados do csv
def populate_total():
    dia_desejado = check_yesterday()  # verifica se tem ontem na db
    ultimo_dia_cadastrado = (
        Dia.objects.all().order_by("-data").first()
    )  # pega o ultimo dia cadastrado (para fazer a insercao recursiva caso necessario)

    todos = []

    if (
        not ultimo_dia_cadastrado or not dia_desejado
    ):  # se nao tiver ontem, ou o ultimo dia (db esta vazia), seleciona todos os casos
        todos = get_new_cases_total()

    if not ultimo_dia_cadastrado:  # Se nao encontrar o ultimo dia (db vazia)
        for dia in todos:
            Dia.objects.create(
                data=dia["date"], casos=int(dia["World"])
            )  # Cria registros para todos os dias

    elif not dia_desejado:  # Se tiver ultimo dia mas nao for ontem
        for dia in todos:
            data = dia["date"].split("-")

            if (
                date(int(data[0]), int(data[1]), int(data[2]))
                > ultimo_dia_cadastrado.data
            ):  # Verifica se o dia do csv, eh maior q a data do ultimo registro cadastrado na db
                Dia.objects.create(data=dia["date"], casos=int(dia["World"]))
