# Analise-de-Faturamento-e-Impostos
 Este repositório contém um script em Python que realiza a análise de faturamento mensal e o cálculo dos impostos correspondentes. Os dados de faturamento são organizados em um dicionário, e o script converte esses valores de string para float, calcula os impostos mensais e trimestrais, e armazena os resultados em um novo dicionário.



### Funcionalidades:
- Conversão de valores monetários: Converte strings formatadas em valores float.
- Cálculo de impostos:
- Imposto Mensal (ISS, PIS e COFINS)
- Imposto Trimestral (IR e CSLL, com adição conforme a faixa de faturamento)
- Resultados organizados: Armazena o faturamento, imposto mensal e imposto trimestral para cada mês.




### Calculos realizados com base nos seguintes valores:
- 5% sobre faturamento de ISS (mensal)
- 0,65% de PIS sobre faturamento, (mensal)
- 3% de COFINS sobre faturmaneto, (mensal)
- 4.8% de IR (trimestral)
- 10% de IR Adicional sobre o que ultrapassar 20mil do faturamento (trimestral)
- CSLL: 2,88% sobre faturamento (trimestral)
