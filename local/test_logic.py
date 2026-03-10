"""
Unit tests for logic.py, using pytest framework
"""

from logic import TaskProcessor, calculate_discount


def test_add_task_logic() -> None:
    """verify if the methods add_task and get_all_task are correct"""
    proc = TaskProcessor()
    proc.add_task("Fix Bug", "High")
    assert len(proc.get_all_tasks()) == 1
    assert proc.get_all_tasks()[0]["title"] == "Fix Bug"


def test_discount_logic() -> None:
    """Verify if the function calculate_discount is correct"""
    result = calculate_discount(100.0, 20.0)
    assert result == 80.0
