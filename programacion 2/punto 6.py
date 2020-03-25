horas = float(input("Introduce tus horas de trabajo: "))
paga_por_hora = float(input("Introduce lo que cobras por hora: "))
paga_total = round(horas * paga_por_hora, 3)
print("Tu paga es " + str(paga_total))
