#include <stdio.h>

// Desafio Batalha Naval - MateCheck
// Este código inicial serve como base para o desenvolvimento do sistema de Batalha Naval.
// Siga os comentários para implementar cada parte do desafio.

// Helper functions for testing
void inicializarTabuleiro(int tamanho, int tabuleiro[tamanho][tamanho]) {
    for (int i = 0; i < tamanho; i++) {
        for (int j = 0; j < tamanho; j++) {
            tabuleiro[i][j] = 0;
        }
    }
}

void posicionarNavioHorizontal(int tamanho, int tabuleiro[tamanho][tamanho], int linha, int coluna, int tamanhoNavio) {
    for (int j = 0; j < tamanhoNavio; j++) {
        if (coluna + j < tamanho) {
            tabuleiro[linha][coluna + j] = 3;
        }
    }
}

void posicionarNavioVertical(int tamanho, int tabuleiro[tamanho][tamanho], int linha, int coluna, int tamanhoNavio) {
    for (int i = 0; i < tamanhoNavio; i++) {
        if (linha + i < tamanho) {
            tabuleiro[linha + i][coluna] = 3;
        }
    }
}

#ifndef RUN_TESTS
int main(void) {
    // Nível Novato - Posicionamento dos Navios
    int tabuleiro[5][5];
    inicializarTabuleiro(5, tabuleiro);

    // Posiciona um navio horizontalmente na linha 1, coluna 1 com tamanho 3
    posicionarNavioHorizontal(5, tabuleiro, 1, 1, 3);

    // Posiciona um navio verticalmente na linha 0, coluna 4 com tamanho 2
    posicionarNavioVertical(5, tabuleiro, 0, 4, 2);

    // Exibição do nível novato
    printf("Tabuleiro Nivel Novato:\n");
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            printf("%d ", tabuleiro[i][j]);
        }
        printf("\n");
    }
    printf("\n");

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
