import builtins
import io
import sys
import pytest

from Lab03Monopoly_changed import (
    get_yes_no,
    get_int_in_range,
    get_nonneg_int,
    main,
)

# Helper to run main with a sequence of inputs and capture output
def run_with_inputs(inputs):
    inputs_iter = iter(inputs)
    def fake_input(prompt=""):
        try:
            return next(inputs_iter)
        except StopIteration:
            raise EOFError("No more input")

    monkeypatch_input = pytest.MonkeyPatch()
    monkeypatch_input.setattr('builtins.input', fake_input)
    captured = io.StringIO()
    monkeypatch_input.setattr('sys.stdout', captured)
    try:
        main()
    except EOFError:
        pass
    finally:
        monkeypatch_input.undo()
    return captured.getvalue()


def test_get_yes_no_valid(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda prompt='': ' y ')
    assert get_yes_no('prompt') == 'y'


def test_get_yes_no_invalid_then_valid(monkeypatch, capsys):
    inputs = iter(['maybe', 'N'])
    monkeypatch.setattr('builtins.input', lambda prompt='': next(inputs))
    # Should return 'n' after re-prompt
    assert get_yes_no('p') == 'n'


def test_get_int_in_range_valid(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda prompt='': '3')
    assert get_int_in_range('p', 0, 5) == 3


def test_get_int_in_range_invalid_then_valid(monkeypatch, capsys):
    inputs = iter(['eight', '10', '4'])
    monkeypatch.setattr('builtins.input', lambda prompt='': next(inputs))
    assert get_int_in_range('p', 0, 5) == 4


def test_get_nonneg_int_valid(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda prompt='': '42')
    assert get_nonneg_int('p') == 42


def test_get_nonneg_int_invalid_then_valid(monkeypatch):
    inputs = iter(['-1', 'foo', '0'])
    monkeypatch.setattr('builtins.input', lambda prompt='': next(inputs))
    assert get_nonneg_int('p') == 0


def test_main_not_owner():
    # Not owner should exit early with message
    output = run_with_inputs(['n'])
    assert 'You must own all three green properties' in output


def test_main_pa_already_hotel():
    # Owner says yes, PA has hotel
    output = run_with_inputs(['y', '5'])
    assert 'Penn Avenue already has a hotel' in output


def test_main_swap_with_nc_hotel():
    # PA has 4, NC has hotel
    # provide pc_status (0) as well so program reaches swap handling
    output = run_with_inputs(['y', '4', '5', '0'])
    assert 'You can swap your North Carolina hotel' in output


def test_main_success_path(monkeypatch):
    # Simulate a full successful run: own, pa=3, nc=2, pc=1, houses available=6, hotels available=1, cash sufficient
    inputs = ['y', '3', '2', '1', '6', '1', '1400']
    out = run_with_inputs(inputs)
    assert 'Congratulations - you can purchase a hotel' in out
    assert 'This will cost:' in out

