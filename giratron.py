import random
import pyttsx3
import time

class Jogo:
    cores = []
    numeros = []

    @staticmethod
    def piscar_sequencia(sequencia):
        for item in sequencia:
            Jogo.falar(item)
            time.sleep(1)

    @staticmethod
    def falar(texto):
        engine = pyttsx3.init()
        engine.say(texto)
        engine.runAndWait()

class Genius(Jogo):
    cores = ['vermelho', 'verde', 'azul', 'amarelo']
    numeros = ['1', '2', '3', '4']

    @classmethod
    def jogar(cls):
        acertos = 0
        nivel = 3  # Nível inicial de complexidade

        while acertos < 3:
            sequencia = random.choices(cls.cores + cls.numeros, k=nivel)
            print(f"Sequência do Genius ({nivel} elementos):")
            cls.piscar_sequencia(sequencia)

            # Lógica para adivinhar a sequência
            palpite = input("Seu palpite (separe as cores e números por espaço): ").lower().split()
            if palpite == sequencia:
                print("Parabéns! Você acertou a sequência. :D")
                acertos += 1
                nivel += 1  # Aumenta a complexidade para a próxima rodada
            else:
                print("Você errou. Tente novamente. :0")


class Giratron(Jogo):
    cores = ['laranja', 'roxo', 'verde', 'amarelo']
    numeros = ['5', '6', '7', '8']

    @classmethod
    def jogar(cls):
        acertos = 0
        nivel = 3  # Nível inicial de complexidade

        while acertos < 3:
            sequencia = random.choices(cls.cores + cls.numeros, k=nivel)
            print(f"Sequência do Giratron ({nivel} elementos):")
            cls.piscar_sequencia(sequencia)

            # Lógica para adivinhar a sequência
            palpite = input("Seu palpite (separe as cores e números por espaço): ").lower().split()
            if palpite == sequencia:
                print("Parabéns! Você acertou a sequência. :D")
                acertos += 1
                nivel += 1  # Aumenta a complexidade para a próxima rodada
            else:
                print("Você errou. Tente novamente. :0")


# Descomente para jogar Genius
Genius.jogar()

# Descomente para jogar Giratron
#Giratron.jogar()
