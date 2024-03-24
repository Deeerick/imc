from alive_progress import alive_bar
import time

def calcular_imc(peso, altura_cm):
    altura_m = altura_cm / 100
    imc = peso / (altura_m ** 2)
    return imc

print('=' * 10 + '\033[91m 🚨 Inicializando a Calculadora de IMC 🚨 \033[0m' + '=' * 10)

peso = float(input("\033[91m > Qual o seu peso em KG?  \033[0m"))
altura_cm = float(input("\033[91m > Qual a sua altura em centímetros?  \033[0m"))

print("\033[91mCalculando seu IMC...\033[0m")
with alive_bar(100) as bar:
    for _ in range(100):
        time.sleep(0.01)
        bar()

imc = calcular_imc(peso, altura_cm)

print("\033[91m > Seu IMC é de {:.1f} \033[0m".format(imc))

if imc < 18:
    print("\033[91m > Classificação = ABAIXO DO PESO \033[0m")
elif 18 <= imc < 25:
    print("\033[91m > Classificação = PESO IDEAL \033[0m")
elif 25 <= imc < 30:
    print("\033[91m > Classificação = SOBREPESO \033[0m")
elif 30.0 <= imc < 35:
    print("\033[91m > Classificação = OBESIDADE I \033[0m")
elif 35 <= imc < 40:
    print("\033[91m > Classificação = OBESIDADE II \033[0m")
elif imc > 40:
    print("\033[91m > Classificação = OBESIDADE III \033[0m")
else:
    print("\033[91m > Por favor, tente novamente! \033[0m")
