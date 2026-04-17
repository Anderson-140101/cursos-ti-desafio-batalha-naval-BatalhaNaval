#include <stdio.h>

// Desafio Batalha Naval - MateCheck
// Este código inicial serve como base para o desenvolvimento do sistema de Batalha Naval.
// Siga os comentários para implementar cada parte do desafio.

#define TAMANHO_TABULEIRO 10

int main() {
    // Nível Novato - Posicionamento dos Navios
    // Nível Aventureiro - Expansão do Tabuleiro e Posicionamento Diagonal
    int tabuleiro[TAMANHO_TABULEIRO][TAMANHO_TABULEIRO] = {0};

    // Navio 1: Vertical (Tamanho 3)
    tabuleiro[2][1] = 3;
    tabuleiro[3][1] = 3;
    tabuleiro[4][1] = 3;

    // Navio 2: Horizontal (Tamanho 3)
    tabuleiro[8][5] = 3;
    tabuleiro[8][6] = 3;
    tabuleiro[8][7] = 3;

    // Navio 3: Diagonal Principal (Tamanho 3)
    tabuleiro[0][0] = 3;
    tabuleiro[1][1] = 3;
    tabuleiro[2][2] = 3;

    // Navio 4: Diagonal Secundária (Tamanho 3)
    tabuleiro[8][1] = 3;
    tabuleiro[7][2] = 3;
    tabuleiro[6][3] = 3;

    // Exibe o tabuleiro completo no console, mostrando 0 para posições vazias e 3 para posições ocupadas.
    printf("Tabuleiro da Batalha Naval:\n");
    for (int i = 0; i < TAMANHO_TABULEIRO; i++) {
        for (int j = 0; j < TAMANHO_TABULEIRO; j++) {
            printf("%d ", tabuleiro[i][j]);
        }
        printf("\n");
    }

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
