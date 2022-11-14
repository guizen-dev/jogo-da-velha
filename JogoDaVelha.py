import numpy as np
import random

print("------JOGO DA VELHA-----\n")
xis = input("Digite o nome do usuário X: ")
bola = input("Digite o nome do usuário ◉: ")

numero = np.array(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
xiscomeco = False
continuar = True
xisganhou = False
escolhax = ""
escolhab = ""
vezx = True
jogadas = 0
velha = False


def layout(array):
    print("\n" + array[0] + " | " + array[1] + " | " + array[2] + "\n── ─── ──\n" + array[3] + " | " + array[
        4] + " | " + array[5] + "\n── ─── ──\n" + array[6] + " | " + array[7] + " | " + array[8] + "\n")


layout(numero)


def continuarr():
    global continuar
    if (numero[0] == "X" and numero[1] == "X" and numero[2] == "X") or (
            numero[3] == "X" and numero[4] == "X" and numero[5] == "X") or (
            numero[6] == "X" and numero[7] == "X" and numero[8] == "X") or (
            numero[0] == "X" and numero[3] == "X" and numero[6] == "X") or (
            numero[1] == "X" and numero[4] == "X" and numero[7] == "X") or (
            numero[2] == "X" and numero[5] == "X" and numero[8] == "X") or (
            numero[0] == "X" and numero[4] == "X" and numero[8] == "X") or (
            numero[2] == "X" and numero[4] == "X" and numero[6] == "X") or (
            numero[0] == "◉" and numero[1] == "◉" and numero[2] == "◉") or (
            numero[3] == "◉" and numero[4] == "◉" and numero[5] == "◉") or (
            numero[6] == "◉" and numero[7] == "◉" and numero[8] == "◉") or (
            numero[0] == "◉" and numero[3] == "◉" and numero[6] == "◉") or (
            numero[1] == "◉" and numero[4] == "◉" and numero[7] == "◉") or (
            numero[2] == "◉" and numero[5] == "◉" and numero[8] == "◉") or (
            numero[0] == "◉" and numero[4] == "◉" and numero[8] == "◉") or (
            numero[2] == "◉" and numero[4] == "◉" and numero[6] == "◉"):
        continuar = False
        return False


def analise(esx, esb, array):
    global vezx

    if vezx:
        if esx.isdigit():
            if int(esx) <= 9:
                if array[int(esx) - 1] != "◉":
                    for i in array:
                        if esx == i:
                            array[int(esx) - 1] = "X"
                            layout(array)
                            vezx = False
                else:
                    print("O seu número já foi selecionado, é maior do que 9 ou não é um número")
                    vezx = True
            else:
                print("O seu número já foi selecionado, é maior do que 9 ou não é um número")
                vezx = True
        else:
            print("O seu número já foi selecionado, é maior do que 9 ou não é um número")
            vezx = True
    else:
        if esb.isdigit():
            if int(esb) <= 9:
                if array[int(esb) - 1] != "X":
                    for i in array:
                        if esb == i:
                            array[int(esb) - 1] = "◉"
                            layout(array)
                            vezx = True
                else:
                    print("O seu número já foi selecionado, é maior do que 9 ou não é um número")
                    vezx = False
            else:
                print("O seu número já foi selecionado, é maior do que 9 ou não é um número")
                vezx = False
        else:
            print("O seu número já foi selecionado, é maior do que 9 ou não é um número")
            vezx = False


def velhaa():
    global jogadas, velha
    jogadas += 1

    if jogadas == 9:
        velha = True


def jogo(x, b):
    # sorteio
    global xiscomeco, escolhab, escolhax, continuar, xisganhou, vezx, velha
    n = random.randint(0, 1)
    if n == 0:
        print("Por sorteio, o usuário " + x + " irá começar.\n")
        xiscomeco = True
    else:
        print("Por sorteio, o usuário " + b + " irá começar.\n")
    #
    #
    #
    #
    # começo caso x for iniciar
    if xiscomeco:
        vezx = True
        while continuar:
            while vezx:
                escolhax = input("Jogador " + x + " escolha um número: ")
                analise(escolhax, escolhab, numero)
            continuarr()
            velhaa()
            if not continuar:
                xisganhou = True
                break
            if velha:
                break
            while not vezx:
                escolhab = input("Jogador " + b + " escolha um número: ")
                analise(escolhax, escolhab, numero)
            continuarr()
            velhaa()
            if not continuar:
                xisganhou = False
                break
            if velha:
                break
        if velha:
            print("O jogo deu velha, recomece!")
        else:
            if xisganhou:
                print("O jogador " + x + " ganhou a partida. Parabéns!")
            elif not xisganhou:
                print("O jogador " + b + " ganhou a partida. Parabéns!")

    #
    #
    #
    # começo caso b for iniciar
    else:
        vezx = False
        while continuar:
            while not vezx:
                escolhab = input("Jogador " + b + " escolha um número: ")
                analise(escolhax, escolhab, numero)
            continuarr()
            velhaa()
            if not continuar:
                xisganhou = False
                break
            if velha:
                break
            while vezx:
                escolhax = input("Jogador " + x + " escolha um número: ")
                analise(escolhax, escolhab, numero)
            continuarr()
            velhaa()
            if not continuar:
                xisganhou = True
                break
            if velha:
                break
        if velha:
            print("O jogo deu velha, recomece!")
        else:
            if not xisganhou:
                print("O jogador " + b + " ganhou a partida. Parabéns!")
            elif xisganhou:
                print("O jogador " + x + " ganhou a partida. Parabéns!")

jogo(xis, bola)