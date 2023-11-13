class FundoImobiliario:
    def __init__(
        self,
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
    ):
        self.codigo = codigo
        self.segmento = segmento
        self.cotacao = cotacao
        self.ffo_yield = ffo_yield
        self.dividend_yield = dividend_yield
        self.p_vp = p_vp
        self.valor_mercado = valor_mercado
        self.liquidez = liquidez
        self.qt_imoveis = qt_imoveis
        self.preco_m2 = preco_m2
        self.aluguel_m2 = aluguel_m2
        self.cap_rate = cap_rate
        self.vacancia = vacancia


class Estrategia:
    def __init__(
        self,
        segmento="",
        cotacao_minima=0,
        ffo_yield_minimo=0,
        dividend_yield_minimo=0,
        p_vp_minimo=0,
        valor_mercado_minimo=0,
        liquidez_minima=0,
        qt_imoveis_minima=0,
        preco_m2_minimo=0,
        aluguel_m2_minimo=0,
        cap_rate_minimo=0,
        maxima_vacancia_media=0,
    ):
        self.segmento = segmento
        self.cotacao_minima = cotacao_minima
        self.ffo_yield_minimo = ffo_yield_minimo
        self.dividend_yield_minimo = dividend_yield_minimo
        self.p_vp_minimo = p_vp_minimo
        self.valor_mercado_minimo = valor_mercado_minimo
        self.liquidez_minima = liquidez_minima
        self.qt_imoveis_minima = qt_imoveis_minima
        self.preco_m2_minimo = preco_m2_minimo
        self.aluguel_m2_minimo = aluguel_m2_minimo
        self.cap_rate_minimo = cap_rate_minimo
        self.maxima_vacancia_media = maxima_vacancia_media

    def aplica_estrategia(self, fundo: FundoImobiliario):
        if self.segmento != "":
            if fundo.segmento != self.segmento:
                return False

        if (
            fundo.cotacao < self.cotacao_minima
            or fundo.ffo_yield < self.ffo_yield_minimo
            or fundo.dividend_yield < self.dividend_yield_minimo
            or fundo.p_vp < self.p_vp_minimo
            or fundo.valor_mercado < self.valor_mercado_minimo
            or fundo.liquidez < self.liquidez_minima
            or fundo.qt_imoveis < self.qt_imoveis_minima
            or fundo.preco_m2 < self.preco_m2_minimo
            or fundo.aluguel_m2 < self.aluguel_m2_minimo
            or fundo.cap_rate < self.cap_rate_minimo
            or fundo.vacancia > self.maxima_vacancia_media
        ):
            return False
