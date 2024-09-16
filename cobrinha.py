import pygame
import random
import sys

# Inicialza o Pygame
pygame.init()

# Dimensões da tela
largura = 600
altura = 400
tela = pygame.display.set.mode((largura, altura))
pygame. display.set.captian('Jogo da Cobrinha')

# Definição de cores
verde = (0, 0, 255)
vermelho = (255, 0, 0)
preto (0, 0, 0)

# Configurações dp jogo
tamanho_celula = 20 
velocidade = 5
relogio = pygame.time.clock()

# Função para gerar a comida em posição aleatória
def gerar_comida():
    x_comida = random.randrange(0, largura, tamanho_celula)
    y_comida = random.randrange(0, altura, tamanho_celula)
    return x_comida, y_comida

# Função para desenhar a cobrinha
def desenhar_cobrinha(cobra)
    for parte in cobra:
        pygame.draw.rect(tela, verde, (parte[0], parte[1], tamanho_celula, tamanho_celula))

# Função principal
def jogo():
    x = largura // 2
    y = altura // 2
    x_velocidade = 0
    y_velocidade = 0
    cobra = [(x, y)]
    comprimento_cobra = 1

    x_comida, y_comida = gerar_comida()

    while True:
        # Detecta eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Captura as teclas para mover a cobrinha
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_LEFT and x_velocidade == 0:
                        x_velocidade = -tamanho_celula
                        y_velocidade = 0
                    elif evento.key == pygame.K_RIGHT and x_velocidade == 0:
                        x_velocidade = tamanho_celula
                        y_velocidade = 0
                    elif evento.key == pygame.K_UP and y_velocidade == 0:
                        y_velocidade = -tamanho_celula
                        x_velocidade = 0
                    elif evento.key == pygame.K_DOWN and y_velocidade == 0:
                        y_velocidade = tamanho_celula
                        x_velocidade = 0
                            
        # Atualiza a posição da cobrinha
        x += x_velocidade
        y += y_velocidade

        # Mantém o tamanha da cobrinha
        if len(cobra) > comprimento_cobra:
            del cobra[0]

        # Detecta colisão com bordas ou com o próprio corpo
        if x < 0 or x>= largura or y < 0 or >= altura or (x, y) in cobra[:-1]:
            break

        #Detecta se a cobrinha comeu a comida
        if x == x_comida and y == y_comida:
            comprimento_cobra += 1
            x_comida, y_comida = gerar_comida()

        #Atualiza a tela
        tela.fill(preto)
        desenhar_cobrinha(cobra)
        pygame.draw.rect(tela, vermelho, (x_comida, y_comida, tamanho_celula, tamanho_celula))
        pygame.display.flip()

        relogio.tick(velocidade)

# Inicia o jojo
jogo()