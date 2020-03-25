inversión = float(input("¿Cantidad a invertir? "))
intereses = float(input("¿Interés porcentual anual? "))
años = int(input("¿Años?"))
print("Capital final: " + str(round(inversión * (intereses / 100 + 1) ** años, 2)))
