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


# Endpoint to check if the QPI is online and working
# go to http://127.0.0.1:8000
@app.get("/")
def read_root() -> Dict[str, str]:
    return {"status": "online", "message": "FastAPI"}


# Endpoint to test the add_task method by using post endpoint
# go to 127.0.0.1:8000/docs -> /tasks/add -> try it out -> *enter parameters* -> execute
@app.post("/tasks/add")
def add_new_task(title: str, priority: str) -> Dict[str, str]:
    result = processor.add_task(title, priority)
    return {"message": result}


# Endpoint to test the get_all_tasks method by using get endpoint
# go to 127.0.0.1:8000/docs -> /tasks/list -> try it out -> execute
@app.get("/tasks/list")
def list_tasks() -> List[Dict[str, str]]:
    """Endpoint to retrieve all tasks."""
    return processor.get_all_tasks()


# Endpoint to test the calculate_discount function by using get endpoint
# go to 127.0.0.1:8000/docs -> /calculate/discount -> try it out -> *enter parameters* -> execute
@app.get("/calculate/discount")
def get_discount(price: float, discount: float) -> Dict[str, Union[str, float]]:
    final_price = calculate_discount(price, discount)
    return {
        "original_price": price,
        "discount_applied": discount,
        "final_price": final_price,
    }
