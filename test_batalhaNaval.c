#include <stdio.h>
#include <assert.h>

// Declare the helper functions from batalhaNaval.c
void inicializarTabuleiro(int tamanho, int tabuleiro[tamanho][tamanho]);
void posicionarNavioHorizontal(int tamanho, int tabuleiro[tamanho][tamanho], int linha, int coluna, int tamanhoNavio);
void posicionarNavioVertical(int tamanho, int tabuleiro[tamanho][tamanho], int linha, int coluna, int tamanhoNavio);

void test_inicializarTabuleiro() {
    int tabuleiro[5][5];
    // Start with non-zero values
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            tabuleiro[i][j] = -1;
        }
    }

    inicializarTabuleiro(5, tabuleiro);

    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            assert(tabuleiro[i][j] == 0);
        }
    }
    printf("test_inicializarTabuleiro passed!\n");
}

void test_posicionarNavioHorizontal() {
    int tabuleiro[5][5];
    inicializarTabuleiro(5, tabuleiro);

    // Position ship at row 1, col 1, size 3
    posicionarNavioHorizontal(5, tabuleiro, 1, 1, 3);

    // Check ship position
    assert(tabuleiro[1][1] == 3);
    assert(tabuleiro[1][2] == 3);
    assert(tabuleiro[1][3] == 3);

    // Check surrounding empty spaces
    assert(tabuleiro[1][0] == 0);
    assert(tabuleiro[1][4] == 0);
    assert(tabuleiro[0][1] == 0);
    assert(tabuleiro[2][1] == 0);

    printf("test_posicionarNavioHorizontal passed!\n");
}

void test_posicionarNavioVertical() {
    int tabuleiro[5][5];
    inicializarTabuleiro(5, tabuleiro);

    // Position ship at row 1, col 2, size 3
    posicionarNavioVertical(5, tabuleiro, 1, 2, 3);

    // Check ship position
    assert(tabuleiro[1][2] == 3);
    assert(tabuleiro[2][2] == 3);
    assert(tabuleiro[3][2] == 3);

    // Check surrounding empty spaces
    assert(tabuleiro[0][2] == 0);
    assert(tabuleiro[4][2] == 0);
    assert(tabuleiro[1][1] == 0);
    assert(tabuleiro[1][3] == 0);

    printf("test_posicionarNavioVertical passed!\n");
}

void test_posicionarNavioOutOfBounds() {
    int tabuleiro[5][5];
    inicializarTabuleiro(5, tabuleiro);

    // Position horizontal ship near boundary
    posicionarNavioHorizontal(5, tabuleiro, 0, 3, 4);

    // Verify it doesn't write out of bounds (handled by the if condition)
    assert(tabuleiro[0][3] == 3);
    assert(tabuleiro[0][4] == 3);
    // 0, 5 and 0, 6 shouldn't be written to

    printf("test_posicionarNavioOutOfBounds passed!\n");
}

int main(void) {
    printf("Running Batalha Naval Tests...\n");
    test_inicializarTabuleiro();
    test_posicionarNavioHorizontal();
    test_posicionarNavioVertical();
    test_posicionarNavioOutOfBounds();
    printf("All tests passed successfully!\n");
    return 0;
}
