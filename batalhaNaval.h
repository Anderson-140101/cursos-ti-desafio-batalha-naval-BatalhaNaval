#ifndef BATALHANAVAL_H
#define BATALHANAVAL_H

#define BOARD_SIZE 10
#define WATER 0
#define SHIP 3
#define ABILITY 1

void inicializarTabuleiro(int tabuleiro[BOARD_SIZE][BOARD_SIZE]);

// orientation: 0 for horizontal, 1 for vertical, 2 for diagonal right-down, 3 for diagonal left-down
int posicionarNavio(int tabuleiro[BOARD_SIZE][BOARD_SIZE], int linha, int coluna, int tamanho, int orientacao);

// 0 for cone, 1 for octahedron, 2 for cross
int aplicarHabilidade(int tabuleiro[BOARD_SIZE][BOARD_SIZE], int linha, int coluna, int tipo_habilidade);

#endif
