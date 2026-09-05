print("Calculadora de Consumo de Energia Elétrica")
#Entrada de dados
nomeAparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência (watts): "))
horasDia = float(input("Digite as horas de uso por dia: "))

#Calculo do consumo mensal em kWh
consumoMensal = (potencia * horasDia * 30) / 1000
custo = consumoMensal * 0.75

#Exibição dos resultados
print()
print("Aparelho:", nomeAparelho)
print("Consumo estimado:", consumoMensal, "kWh/mês")
print("Custo estimado: R$", custo)