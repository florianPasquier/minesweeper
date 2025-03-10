import pytest
import src.minesweeper as minesweeper


@pytest.fixture
def gametest():
    return minesweeper.Minesweeper(3, 3, 2)


def test_module_exists():
    assert minesweeper


def test_place_mines(gametest):
    game = gametest
    game.place_mines()
    assert len(game.mines) == 2


def test_reveal(gametest):
    import random

    random.seed(0)
    game = gametest
    game.place_mines()
    game.reveal(2, 2)
    assert game.revealed == {(2, 2)}


def test_get_board(gametest):
    game = gametest
    game.place_mines()
    game.reveal(2, 2)
    board = game.get_board()
    assert board[2][2] == 0


def test_is_winner(gametest):
    game = gametest
    game.place_mines()
    game.reveal(2, 2)
    assert not game.is_winner()
    game.reveal(0, 0)
    game.reveal(0, 1)
    game.reveal(0, 2)
    game.reveal(1, 0)
    game.reveal(1, 1)
    game.reveal(1, 2)
    assert game.is_winner()


def test_restart(gametest):
    game = gametest
    game.place_mines()
    game.reveal(2, 2)
    game.restart()
    assert game.revealed == set()
    assert len(game.mines) == 2
    assert game.rows == 3
    assert game.cols == 3
    assert game.num_mines == 2
