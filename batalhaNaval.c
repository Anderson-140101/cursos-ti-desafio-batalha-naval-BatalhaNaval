#include <stdio.h>

// Desafio Batalha Naval - MateCheck
// Este código inicial serve como base para o desenvolvimento do sistema de Batalha Naval.
// Siga os comentários para implementar cada parte do desafio.

int main() {
    // Nível Novato - Posicionamento dos Navios
    // Sugestão: Declare uma matriz bidimensional para representar o tabuleiro (Ex: int tabuleiro[5][5];).
    // Sugestão: Posicione dois navios no tabuleiro, um verticalmente e outro horizontalmente.
    // Sugestão: Utilize `printf` para exibir as coordenadas de cada parte dos navios.

    // Nível Aventureiro - Expansão do Tabuleiro e Posicionamento Diagonal
    // Sugestão: Expanda o tabuleiro para uma matriz 10x10.
    int tabuleiro[10][10] = {0};

    // Navio 1: Horizontal (Tamanho 3)
    tabuleiro[2][2] = 3;
    tabuleiro[2][3] = 3;
    tabuleiro[2][4] = 3;

    // Navio 2: Vertical (Tamanho 3)
    tabuleiro[5][1] = 3;
    tabuleiro[6][1] = 3;
    tabuleiro[7][1] = 3;

    printf("Coordenadas do Navio Horizontal:\n");
    printf("Linha 2, Coluna 2\n");
    printf("Linha 2, Coluna 3\n");
    printf("Linha 2, Coluna 4\n\n");

    printf("Coordenadas do Navio Vertical:\n");
    printf("Linha 5, Coluna 1\n");
    printf("Linha 6, Coluna 1\n");
    printf("Linha 7, Coluna 1\n\n");

    // Sugestão: Posicione quatro navios no tabuleiro, incluindo dois na diagonal.
    // Navio 3: Diagonal Principal (Tamanho 3)
    tabuleiro[6][6] = 3;
    tabuleiro[7][7] = 3;
    tabuleiro[8][8] = 3;

    // Navio 4: Diagonal Secundária (Tamanho 3)
    tabuleiro[0][9] = 3;
    tabuleiro[1][8] = 3;
    tabuleiro[2][7] = 3;

    // Sugestão: Exiba o tabuleiro completo no console, mostrando 0 para posições vazias e 3 para posições ocupadas.
    printf("Tabuleiro 10x10:\n");
    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < 10; j++) {
            printf("%d ", tabuleiro[i][j]);
        }
        printf("\n");
    }
    printf("\n");

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
