import time
import random
import PySimpleGUI as sg
import os
import pygame
import threading


class PassGen:
    def __init__(self):
        # Layout
        sg.theme('Black')
        layout = [
            [sg.Text('Site/Software', size=(10, 1)),
             sg.Input(key='site', size=(20, 1))],
            [sg.Text('Email/Usuario', size=(10, 1)),
             sg.Input(key='usuario', size=(20, 1))],
            [sg.Text('Quantidade de caracteres'), sg.Combo(values=list(
                range(30)), key='total_chars', default_value=1, size=(3, 1))],
            [sg.Output(size=(32, 5))],
            [sg.Button('Gerar Senha')]

        ]
        # Janela
        self.janela = sg.Window('Password Generator', layout)

    def tocar_som(self):
        pygame.mixer.init()
        sound = pygame.mixer.Sound("sound.mp3")
        sound.set_volume(0.5)
        while True:  # Loop infinito para repetir o áudio
            sound.play()
            while pygame.mixer.get_busy():  # Espera o áudio terminar antes de repetir
                pygame.time.Clock().tick(10)  # Pequena pausa para evitar consumo excessivo de CPU

    def Iniciar(self):
        self.thread_som = threading.Thread(target=self.tocar_som)
        self.thread_som.daemon = True
        self.thread_som.start()

        while True:
            evento, valores = self.janela.read()
            if evento == sg.WINDOW_CLOSED:
                pygame.mixer.quit()
                break
            if evento == 'Gerar Senha':
                nova_senha = self.gerar_senha(valores)
                print(nova_senha)
                self.salvar_senha(nova_senha, valores)

    def gerar_senha(self, valores):
        char_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%¨&*'
        chars = random.choices(char_list, k=(valores['total_chars']))
        new_pass = ''.join(chars)
        return new_pass

    def salvar_senha(self, nova_senha, valores):
        with open('senhas.txt', 'a', newline='') as arquivo:
            arquivo.write(
                f"site: {valores['site']}\nusuario: {valores['usuario']}\nnova senha: {nova_senha}\n\n")

        print('Arquivo salvo!')


gen = PassGen()
gen.Iniciar()
