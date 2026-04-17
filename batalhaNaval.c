#include <stdio.h>
#include "batalhaNaval.h"

void inicializarTabuleiro(int tabuleiro[BOARD_SIZE][BOARD_SIZE]) {
    for (int i = 0; i < BOARD_SIZE; i++) {
        for (int j = 0; j < BOARD_SIZE; j++) {
            tabuleiro[i][j] = WATER;
        }
    }
}

int posicionarNavio(int tabuleiro[BOARD_SIZE][BOARD_SIZE], int linha, int coluna, int tamanho, int orientacao) {
    // Verificar limites
    for (int i = 0; i < tamanho; i++) {
        int r = linha;
        int c = coluna;

        if (orientacao == 0) { // Horizontal
            c += i;
        } else if (orientacao == 1) { // Vertical
            r += i;
        } else if (orientacao == 2) { // Diagonal right-down
            r += i;
            c += i;
        } else if (orientacao == 3) { // Diagonal left-down
            r += i;
            c -= i;
        } else {
            return 0; // Orientacao invalida
        }

        if (r < 0 || r >= BOARD_SIZE || c < 0 || c >= BOARD_SIZE) {
            return 0; // Fora dos limites
        }
    }

    // Posicionar
    for (int i = 0; i < tamanho; i++) {
        int r = linha;
        int c = coluna;

        if (orientacao == 0) { // Horizontal
            c += i;
        } else if (orientacao == 1) { // Vertical
            r += i;
        } else if (orientacao == 2) { // Diagonal right-down
            r += i;
            c += i;
        } else if (orientacao == 3) { // Diagonal left-down
            r += i;
            c -= i;
        }

        tabuleiro[r][c] = SHIP;
    }

    return 1;
}

int aplicarHabilidade(int tabuleiro[BOARD_SIZE][BOARD_SIZE], int linha, int coluna, int tipo_habilidade) {
    if (linha < 0 || linha >= BOARD_SIZE || coluna < 0 || coluna >= BOARD_SIZE) {
        return 0;
    }

    if (tipo_habilidade == 0) { // Cone
        // 0 0 1 0 0
        // 0 1 1 1 0
        // 1 1 1 1 1
        int matriz[3][5] = {
            {0, 0, 1, 0, 0},
            {0, 1, 1, 1, 0},
            {1, 1, 1, 1, 1}
        };
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 5; j++) {
                if (matriz[i][j] == 1) {
                    int r = linha + i - 0; // -0 to make tip at the given (linha, coluna)? Actually let's assume the center of the base or the tip. Let's make (linha, coluna) the tip. So the tip is at i=0, j=2.
                    int c = coluna + j - 2;
                    if (r >= 0 && r < BOARD_SIZE && c >= 0 && c < BOARD_SIZE) {
                        tabuleiro[r][c] = ABILITY;
                    }
                }
            }
        }
    } else if (tipo_habilidade == 1) { // Octaedro
        // 0 0 1 0 0
        // 0 1 1 1 0
        // 0 0 1 0 0
        int matriz[3][5] = {
            {0, 0, 1, 0, 0},
            {0, 1, 1, 1, 0},
            {0, 0, 1, 0, 0}
        };
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 5; j++) {
                if (matriz[i][j] == 1) {
                    int r = linha + i - 1; // center is i=1, j=2
                    int c = coluna + j - 2;
                    if (r >= 0 && r < BOARD_SIZE && c >= 0 && c < BOARD_SIZE) {
                        tabuleiro[r][c] = ABILITY;
                    }
                }
            }
        }
    } else if (tipo_habilidade == 2) { // Cruz
        // 0 0 1 0 0
        // 1 1 1 1 1
        // 0 0 1 0 0
        int matriz[3][5] = {
            {0, 0, 1, 0, 0},
            {1, 1, 1, 1, 1},
            {0, 0, 1, 0, 0}
        };
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 5; j++) {
                if (matriz[i][j] == 1) {
                    int r = linha + i - 1; // center is i=1, j=2
                    int c = coluna + j - 2;
                    if (r >= 0 && r < BOARD_SIZE && c >= 0 && c < BOARD_SIZE) {
                        tabuleiro[r][c] = ABILITY;
                    }
                }
            }
        }
    } else {
        return 0; // Habilidade invalida
    }
    return 1;
}

// Desafio Batalha Naval - MateCheck
// Este código inicial serve como base para o desenvolvimento do sistema de Batalha Naval.
// Siga os comentários para implementar cada parte do desafio.

#ifndef RUN_TESTS
int main() {
    // Nível Novato - Posicionamento dos Navios
    // Sugestão: Declare uma matriz bidimensional para representar o tabuleiro (Ex: int tabuleiro[5][5];).
    // Sugestão: Posicione dois navios no tabuleiro, um verticalmente e outro horizontalmente.
    // Sugestão: Utilize `printf` para exibir as coordenadas de cada parte dos navios.

    // Nível Aventureiro - Expansão do Tabuleiro e Posicionamento Diagonal
    // Sugestão: Expanda o tabuleiro para uma matriz 10x10.
    // Sugestão: Posicione quatro navios no tabuleiro, incluindo dois na diagonal.
    // Sugestão: Exiba o tabuleiro completo no console, mostrando 0 para posições vazias e 3 para posições ocupadas.

    // Nível Mestre - Habilidades Especiais com Matrizes
    // Sugestão: Crie matrizes para representar habilidades especiais como cone, cruz, e octaedro.
    // Sugestão: Utilize estruturas de repetição aninhadas para preencher as áreas afetadas por essas habilidades no tabuleiro.
    // Sugestão: Exiba o tabuleiro com as áreas afetadas, utilizando 0 para áreas não afetadas e 1 para áreas atingidas.

    // Exemplos de exibição das habilidades:
    // Exemplo para habilidade em cone:
    // 0 0 1 0 0
    // 0 1 1 1 0
    // 1 1 1 1 1
    
    // Exemplo para habilidade em octaedro:
    // 0 0 1 0 0
    // 0 1 1 1 0
    // 0 0 1 0 0

    // Exemplo para habilidade em cruz:
    // 0 0 1 0 0
    // 1 1 1 1 1
    // 0 0 1 0 0

    return 0;
}
#endif
