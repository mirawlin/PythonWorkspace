import pytest

from src.bowling_game.game import Game


def test_score_of_gutter_game_should_be_zero():
    game = Game()

    play_game(game, 20, 0)
    score = game.score()

    assert score == 0


def test_game_with_all_1_pins_should_have_score_20():
    game = Game()

    play_game(game, 20, 1)
    score = game.score()

    assert score == 20


def play_game(game: Game, rolls: int, pins: int):
    for i in range(0, rolls):
        game.roll(pins)
