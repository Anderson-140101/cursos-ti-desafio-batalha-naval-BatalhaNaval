#include <stdio.h>
#include <assert.h>
#include "batalhaNaval.h"

void test_inicializarTabuleiro() {
    int tabuleiro[BOARD_SIZE][BOARD_SIZE];
    // Put dummy data
    tabuleiro[0][0] = 5;

    inicializarTabuleiro(tabuleiro);

    for (int i = 0; i < BOARD_SIZE; i++) {
        for (int j = 0; j < BOARD_SIZE; j++) {
            assert(tabuleiro[i][j] == WATER);
        }
    }
    printf("test_inicializarTabuleiro passed!\n");
}

void test_posicionarNavio() {
    int tabuleiro[BOARD_SIZE][BOARD_SIZE];
    inicializarTabuleiro(tabuleiro);

    // Test horizontal placement
    int res1 = posicionarNavio(tabuleiro, 0, 0, 3, 0); // 3 length horizontal at 0,0
    assert(res1 == 1);
    assert(tabuleiro[0][0] == SHIP);
    assert(tabuleiro[0][1] == SHIP);
    assert(tabuleiro[0][2] == SHIP);
    assert(tabuleiro[0][3] == WATER); // check bounds

    // Test vertical placement
    int res2 = posicionarNavio(tabuleiro, 2, 2, 4, 1); // 4 length vertical at 2,2
    assert(res2 == 1);
    assert(tabuleiro[2][2] == SHIP);
    assert(tabuleiro[3][2] == SHIP);
    assert(tabuleiro[4][2] == SHIP);
    assert(tabuleiro[5][2] == SHIP);
    assert(tabuleiro[6][2] == WATER);

    // Test diagonal right-down
    int res3 = posicionarNavio(tabuleiro, 5, 5, 3, 2); // 3 length diag right-down at 5,5
    assert(res3 == 1);
    assert(tabuleiro[5][5] == SHIP);
    assert(tabuleiro[6][6] == SHIP);
    assert(tabuleiro[7][7] == SHIP);

    // Test out of bounds (horizontal)
    int res4 = posicionarNavio(tabuleiro, 0, 8, 3, 0); // starts at 0,8 needs up to 0,10 (out of bounds)
    assert(res4 == 0);
    // Ensure it didn't partially write
    assert(tabuleiro[0][8] == WATER);

    // Test out of bounds (vertical)
    int res5 = posicionarNavio(tabuleiro, 8, 0, 3, 1);
    assert(res5 == 0);
    assert(tabuleiro[8][0] == WATER);

    printf("test_posicionarNavio passed!\n");
}

void test_aplicarHabilidade() {
    int tabuleiro[BOARD_SIZE][BOARD_SIZE];
    inicializarTabuleiro(tabuleiro);

    // Test cone
    int res1 = aplicarHabilidade(tabuleiro, 2, 2, 0);
    assert(res1 == 1);
    assert(tabuleiro[2][2] == ABILITY);
    assert(tabuleiro[3][1] == ABILITY);
    assert(tabuleiro[3][2] == ABILITY);
    assert(tabuleiro[3][3] == ABILITY);
    assert(tabuleiro[4][0] == ABILITY);
    assert(tabuleiro[4][1] == ABILITY);
    assert(tabuleiro[4][2] == ABILITY);
    assert(tabuleiro[4][3] == ABILITY);
    assert(tabuleiro[4][4] == ABILITY);

    // Test out of bounds origin
    int res2 = aplicarHabilidade(tabuleiro, -1, 5, 0);
    assert(res2 == 0);

    // Test invalid ability type
    int res3 = aplicarHabilidade(tabuleiro, 5, 5, 3);
    assert(res3 == 0);

    printf("test_aplicarHabilidade passed!\n");
}

int main() {
    printf("Running tests...\n");
    test_inicializarTabuleiro();
    test_posicionarNavio();
    test_aplicarHabilidade();
    printf("All tests passed successfully!\n");
    return 0;
}
