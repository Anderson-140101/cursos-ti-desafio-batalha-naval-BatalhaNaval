
#include <stdio.h>
#include <stdlib.h>

// --- Constantes para o Tabuleiro ---
#define LINHAS_NOVATO 8
#define COLUNAS_NOVATO 8

// --- Representação do Tabuleiro ---
#define AGUA 0
#define NAVIO 1

/**
 * @brief Função para inicializar o tabuleiro com água.
 * @param linhas Número de linhas do tabuleiro.
 * @param colunas Número de colunas do tabuleiro.
 * @param tabuleiro A matriz que representa o tabuleiro.
 */
void inicializarTabuleiro(int linhas, int colunas, int tabuleiro[linhas][colunas]) {
    for (int i = 0; i < linhas; i++) {
        for (int j = 0; j < colunas; j++) {
            tabuleiro[i][j] = AGUA;
        }
    }
}

/**
 * @brief Função para imprimir o tabuleiro no console.
 * @param linhas Número de linhas do tabuleiro.
 * @param colunas Número de colunas do tabuleiro.
 * @param tabuleiro A matriz que representa o tabuleiro.
 */
void imprimirTabuleiro(int linhas, int colunas, int tabuleiro[linhas][colunas]) {
    printf("\n   ");
    for (int j = 0; j < colunas; j++) {
        printf("%d ", j);
    }
    printf("\n");
    printf("  +-");
    for (int j = 0; j < colunas; j++) {
        printf("--");
    }
    printf("+\n");

    for (int i = 0; i < linhas; i++) {
        printf("%d | ", i);
        for (int j = 0; j < colunas; j++) {
            printf("%d ", tabuleiro[i][j]);
        }
        printf("|\n");
    }
     printf("  +-");
    for (int j = 0; j < colunas; j++) {
        printf("--");
    }
    printf("+\n");
}

/**
 * @brief Adiciona um navio no tabuleiro.
 * @param linha_inicial Linha inicial.
 * @param coluna_inicial Coluna inicial.
 * @param tamanho Tamanho do navio.
 * @param horizontal 1 para horizontal, 0 para vertical.
 * @param linhas Total de linhas do tabuleiro.
 * @param colunas Total de colunas do tabuleiro.
 * @param tabuleiro A matriz do tabuleiro.
 */
void adicionarNavio(int linha_inicial, int coluna_inicial, int tamanho, int orientacao, int linhas, int colunas, int tabuleiro[linhas][colunas]) {
    for (int i = 0; i < tamanho; i++) {
        if (orientacao == 1) { // Horizontal
            if (coluna_inicial + i < colunas) {
                tabuleiro[linha_inicial][coluna_inicial + i] = NAVIO;
            }
        } else { // Vertical
            if (linha_inicial + i < linhas) {
                tabuleiro[linha_inicial + i][coluna_inicial] = NAVIO;
            }
        }
    }
}


int main() {
    printf("### Desafio Batalha Naval - MetaCheck ###\n");

    // =================================================================
    // Nível Novato - Posicionamento dos Navios (8x8)
    // =================================================================
    printf("\n// Nível Novato - Tabuleiro 8x8\n");
    
    // Sugestão: Declare uma matriz bidimensional para representar o tabuleiro (8x8 ou 5x5).
    int tabuleiroNovato[LINHAS_NOVATO][COLUNAS_NOVATO];
    
    // Sugestão: Inicie o tabuleiro com '0' para água.
    inicializarTabuleiro(LINHAS_NOVATO, COLUNAS_NOVATO, tabuleiroNovato);

    // Sugestão: Defina a posição dos navios, trocando '0' por '1' manualmente.
    // Sugestão: Utilize 'printf' para exibir as coordenadas de cada parte dos navios.
    adicionarNavio(1, 1, 3, 1, LINHAS_NOVATO, COLUNAS_NOVATO, tabuleiroNovato); // Navio horizontal de tamanho 3
    adicionarNavio(3, 4, 4, 1, LINHAS_NOVATO, COLUNAS_NOVATO, tabuleiroNovato); // Navio horizontal de tamanho 4
    adicionarNavio(5, 2, 2, 1, LINHAS_NOVATO, COLUNAS_NOVATO, tabuleiroNovato); // Navio vertical de tamanho 2
    
    imprimirTabuleiro(LINHAS_NOVATO, COLUNAS_NOVATO, tabuleiroNovato);

    return 0;
}
