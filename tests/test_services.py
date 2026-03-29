import pytest
from app.services import calculate_calories


def test_calculate_calories_fat_loss():
    assert calculate_calories(70, "FL") == 1540


def test_calculate_calories_muscle_gain():
    assert calculate_calories(80, "MG") == 2800


def test_calculate_calories_beginner():
    assert calculate_calories(60, "BG") == 1560


def test_invalid_program():
    with pytest.raises(ValueError):
        calculate_calories(70, "XYZ")


def test_negative_weight():
    with pytest.raises(ValueError):
        calculate_calories(-50, "FL")