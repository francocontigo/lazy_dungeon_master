import pytest
from lazydm.utils.encounters import encounter_level_number_of_players


@pytest.mark.unit
@pytest.mark.high
def test_encounter_same_level_players():
    encounter = encounter_level_number_of_players([[4, 4]])
    assert encounter == [500, 1000, 1500, 2000]


@pytest.mark.unit
@pytest.mark.high
def test_encounter_diferrent_level_players():
    encounter = encounter_level_number_of_players([[2, 4], [2, 5]])
    assert encounter == [750, 1500, 2250, 3200]


@pytest.mark.unit
@pytest.mark.high
def test_encounter_empty():
    encounter = encounter_level_number_of_players([])
    assert encounter == []


@pytest.mark.unit
@pytest.mark.high
def test_encounter_missing_argument():
    encounter = encounter_level_number_of_players([[1]])
    assert encounter == []
