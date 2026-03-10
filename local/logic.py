"""
A little example of a basic program to test the pre-commit configuration
Logic module for processing tasks and calculations.

This module provides a TaskProcessor class to manage task priorities
and a utility function for formatting greeting messages.
"""

from typing import List, Dict


class TaskProcessor:
    """Handles the organization and filtering of user tasks."""

    def __init__(self) -> None:
        """Initializes the processor with an empty task list."""
        self.tasks: List[Dict[str, str]] = []

    def add_task(self, title: str, priority: str) -> str:
        """Adds a new task to the internal storage.

        Args:
            title: The English name of the task.
            priority: Level of importance (High, Medium, Low).

        Returns:
            A confirmation message.
        """
        self.tasks.append({"title": title, "priority": priority})
        return f"Task '{title}' added with {priority} priority."

    def get_all_tasks(self) -> List[Dict[str, str]]:
        """Returns the full list of tasks.

        Returns:
            A list of dictionaries containing task details.
        """
        return self.tasks


def calculate_discount(price: float, discount_percent: float) -> float:
    """Calculates the final price after applying a discount.

    Args:
        price: The initial price of the item.
        discount_percent: The percentage to subtract (0 to 100).

    Returns:
        The discounted price as a float.
    """
    return price * (1 - (discount_percent / 100))
