import requests
import bs4
from tabulate import tabulate
import locale

from models import Estrategia, FundoImobiliario

locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")


def format_percentage(percentage_str):
    return locale.atof(percentage_str.split("%")[0])


def format_decimal(decimal_str):
    return locale.atof(decimal_str)


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

response = requests.get("https://fundamentus.com.br/fii_resultado.php", headers=headers)

soup = bs4.BeautifulSoup(response.text, "html.parser")

lines = soup.find(id="tabelaResultado").find("tbody").find_all("tr")

result = []

estrategia = Estrategia(
    cotacao_minima=50,
    dividend_yield_minimo=3,
    p_vp_minimo=1.0,
    valor_mercado_minimo=10000,
    liquidez_minima=1000,
    qt_imoveis_minima=0,
    preco_m2_minimo=10,
    aluguel_m2_minimo=10,
    cap_rate_minimo=0,
)

for line in lines:
    data = line.find_all("td")
    codigo = data[0].text
    segmento = data[1].text
    cotacao = format_decimal(data[2].text)
    ffo_yield = format_percentage(data[3].text)
    dividend_yield = format_percentage(data[4].text)
    p_vp = format_decimal(data[5].text)
    valor_mercado = format_decimal(data[6].text)
    liquidez = format_decimal(data[7].text)
    qt_imoveis = int(data[8].text)
    preco_m2 = format_decimal(data[9].text)
    aluguel_m2 = format_decimal(data[10].text)
    cap_rate = format_percentage(data[11].text)
    vacancia = format_percentage(data[12].text)

    fundo_imobiliario = FundoImobiliario(
        codigo,
        segmento,
        cotacao,
        ffo_yield,
        dividend_yield,
        p_vp,
        valor_mercado,
        liquidez,
        qt_imoveis,
        preco_m2,
        aluguel_m2,
        cap_rate,
        vacancia,
    )

    if estrategia.aplica_estrategia(fundo_imobiliario):
        result.append(fundo_imobiliario)

header = ["Código", "Segmento", "Cotação", "Dividend Yield"]

table = []

for element in result:
    table.append(
        [
            element.codigo,
            element.segmento,
            element.cotacao,
            element.dividend_yield,
        ]
    )


print(tabulate(table, header, tablefmt="fancy_grid", showindex="always"))
