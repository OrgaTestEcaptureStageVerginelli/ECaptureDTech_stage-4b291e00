"""
Main FastAPI application entry point.

Provides endpoints to interact with the logic.py
and test the different function and class
"""

from fastapi import FastAPI
from typing import List, Dict, Union
from logic import TaskProcessor, calculate_discount

app = FastAPI()
processor = TaskProcessor()  # initiate FastAPI and an object of the class TaskProcessor
# Run fastapi dev to run the server


@app.get("/")
def read_root() -> Dict[str, str]:
    """Endpoint to check if the QPI is online and working
    go to http://127.0.0.1:8000

        Returns:
            A simple status message indicating the API is online.
    """
    return {"status": "online", "message": "FastAPI"}


@app.post("/tasks/add")
def add_new_task(title: str, priority: str) -> Dict[str, str]:
    """Endpoint to test the add_task method by using post endpoint
    go to 127.0.0.1:8000/docs -> /tasks/add -> try it out -> *enter parameters* -> execute

        Args:
            title: The English name of the task.
            priority: Level of importance (High, Medium, Low).
        Returns:
            A confirmation message.
    """
    result = processor.add_task(title, priority)
    return {"message": result}


@app.get("/tasks/list")
def list_tasks() -> List[Dict[str, str]]:
    """Endpoint to test the get_all_tasks method by using get endpoint
    go to 127.0.0.1:8000/docs -> /tasks/list -> try it out -> execute

        Returns:
            A list of dictionaries containing task details.
    """
    return processor.get_all_tasks()


@app.get("/calculate/discount")
def get_discount(price: float, discount: float) -> Dict[str, Union[str, float]]:
    """Endpoint to test the calculate_discount function by using get endpoint
    go to 127.0.0.1:8000/docs -> /calculate/discount -> try it out -> *enter parameters* -> execute

        Args:
            price: The initial price of the item.
            discount_percent: The percentage to subtract (0 to 100).
        Returns:
            The different price values in a dictionary: original price, discount applied and final price after discount.
    """
    final_price = calculate_discount(price, discount)
    return {
        "original_price": price,
        "discount_applied": discount,
        "final_price": final_price,
    }
