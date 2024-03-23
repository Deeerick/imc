print('=' * 10 + '\033[91m 🚨 Inicializando a Calculadora de IMC 🚨 \033[0m' + '=' * 10)

peso = float(input("\033[91m > Qual o seu peso em KG?  \033[0m"))
altura_cm = float(input("\033[91m > Qual a sua altura em centímetros?  \033[0m"))

altura_m = altura_cm / 100
imc = peso / (altura_m ** 2)

print("\033[91m > Seu IMC é de {:.1f} \033[0m".format(imc))

if imc < 18.5:
    print("\033[91m > Classificação = MAGREZA \033[0m")
elif 18.5 <= imc < 24.9:
    print("\033[91m > Classificação = NORMAL \033[0m")
elif 25.0 <= imc < 29.9:
    print("\033[91m > Classificação = SOBREPESO \033[0m")
elif 30.0 <= imc < 39.9:
    print("\033[91m > Classificação = OBESIDADE \033[0m")
else:
    print("\033[91m > Classificação = OBESIDADE GRAVE \033[0m")