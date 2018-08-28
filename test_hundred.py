from hundred import *
import pytest


# test roll will return <= 6
def test_roll_less_6():
    for i in range(100):
        assert roll() <= 6


# test roll will return <= 1
def test_roll_more_1():
    for i in range(100):
        assert roll() >= 1


# test is_game_over to return false
@pytest.mark.parametrize("player_score, computer_score, target", [
    (10, 10, 100),
    (99, 99, 100)
])
def test_game_over_false_norm(player_score, computer_score, target):
    assert is_game_over(player_score, computer_score, target) is False


# test is_game_over to return false when scores tied
def test_game_over_false_tie():
    assert is_game_over(100, 100, 100) is False


# test is_game_over to return true
@pytest.mark.parametrize("player_score, computer_score, target", [
    (100, 0, 100),
    (99, 100, 100)
])
def test_game_over_true(player_score, computer_score, target):
    assert is_game_over(player_score, computer_score, target) is True


# test various score scenarios to check return value of assess_play
@pytest.mark.parametrize("player_score, computer_score, total", [
    (80, 80, 10),
    (80, 80, 0),
    (50, 20, 5),
    (12, 0, 0)
])
def test_assess_6(player_score, computer_score, total):
    assert assess_play(player_score, computer_score, total) == 6


@pytest.mark.parametrize("player_score, computer_score, total", [
    (90, 64, 10),
    (80, 69, 0),
    (80, 50, 15),
    (80, 10, 0),
    (90, 64, 10),
    (10, 6, 2),
    (20, 17, 9),
    (10, 19, 20)
])
def test_assess_not_6(player_score, computer_score, total):
    assert assess_play(player_score, computer_score, total) != 6


@pytest.mark.parametrize("player_score, computer_score, total", [
    (80, 69, 0),
    (80, 50, 15),

])
def test_assess_8(player_score, computer_score, total):
    assert assess_play(player_score, computer_score, total) == 8


@pytest.mark.parametrize("player_score, computer_score, total", [
    (80, 10, 0),
    (90, 64, 10),
    (80, 80, 10),
    (80, 80, 0),
    (50, 20, 5),
    (12, 0, 0)
])
def test_assess_not_8(player_score, computer_score, total):
    assert assess_play(player_score, computer_score, total) != 8


@pytest.mark.parametrize("player_score, computer_score, total", [
    (80, 10, 0),
    (90, 64, 10)
])
def test_assess_9(player_score, computer_score, total):
    assert assess_play(player_score, computer_score, total) == 9


@pytest.mark.parametrize("player_score, computer_score, total", [
    (80, 80, 10),
    (80, 80, 0),
    (50, 20, 5),
    (12, 0, 0)
])
def test_assess_not_9(player_score, computer_score, total):
    assert assess_play(player_score, computer_score, total) != 9


@pytest.mark.parametrize("player_score, computer_score, total", [
    (10, 6, 2),
    (20, 17, 9),
    (10, 19, 20)
])
def test_risk_5(player_score, computer_score, total):
    assert assess_play(player_score, computer_score, total) == 5


@pytest.mark.parametrize("player_score, computer_score, total", [
    (80, 10, 0),
    (90, 64, 10),
    (80, 80, 10),
    (80, 80, 0),
    (50, 20, 5),
    (12, 0, 0)
])
def test_risk_5(player_score, computer_score, total):
    assert assess_play(player_score, computer_score, total) != 5


# set argument to random.seed in roll to 2
@pytest.mark.xfail
def test_move_fixed():
    assert computer_move(10, 10, 100) == 0
    assert human_move(10, 10, 100) == 0
