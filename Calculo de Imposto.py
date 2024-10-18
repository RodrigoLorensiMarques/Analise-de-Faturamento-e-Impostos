faturamento = {
    'jan': 'R$ 95.141,98',
    'fev': 'R$ 95.425,16',
    'mar': 'R$ 89.716,31',
    'abr': 'R$ 78.459,99',
    'mai': 'R$ 71.087,28',
    'jun': 'R$ 83.911,06',
    'jul': 'R$ 56.467,26',
    'ago': 'R$ 88.513,58',
    'set': 'R$ 66.552,49',
    'out': 'R$ 80.164,07',
    'nov': 'R$ 66.964,33',
    'dez': 'R$ 71.525,25',
}

# <--------TASK -------->
# Inserir no sistema um dicionário no formato:

# resultado = {
#     'mes': (faturamento, imposto_mensal, imposto_trimestral),
# }


def ConverteFloat (faturamento_str):
    faturamento_float = float(faturamento_str[3:].replace('.', '').replace(',', '.'))
    return faturamento_float


def Calc_ImpostoMensal(faturamento):
    ISS = 5/100*faturamento
    PIS = 0.65/100*faturamento
    COFINS = 3/100*faturamento
    Soma_ImpostoMensal= ISS+PIS+COFINS
    return Soma_ImpostoMensal

def Calc_ImpostoTrimestral (faturamento):
    IR=4.8/100*faturamento
    CSLL= 2.88/100*faturamento
    IR_ADD=0
    if faturamento >20000:
           IR_ADD=10/100*faturamento
    Soma_ImpostoTrimestral= IR+IR_ADD+CSLL
    return Soma_ImpostoTrimestral


resultado= {}

for chave, faturamento_str in faturamento.items():
    faturamento_float = ConverteFloat (faturamento_str)
    ImpostoMensal= Calc_ImpostoMensal(faturamento_float)
    ImpostoTrimestral = Calc_ImpostoTrimestral(faturamento_float)

    resultado[chave]=(faturamento_float,ImpostoMensal,ImpostoTrimestral)


print (resultado)