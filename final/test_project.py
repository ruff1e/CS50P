from project import add, remove, view
import pytest

tasks = []


def test_add():
    tasks = []
    add("TEST TEST", tasks)
    assert len(tasks) == 1
    assert tasks[0]["id"] ==1
    assert tasks[0]["name"] =="TEST TEST"

def test_add_mul():
    tasks = []
    add("TEST 1", tasks)
    add("TEST 2", tasks)
    assert len(tasks) ==2
    assert tasks[1]["id"] ==2
    assert tasks[1]["name"] =="TEST 2"


def test_removeInvalid():
    tasks = []
    add("TEST INVALID", tasks)
    remove(5, tasks)
    assert len(tasks) ==1
    assert tasks[0]["name"] == "TEST INVALID"


def test_reassign():
    tasks = []
    add("A", tasks)
    add("B", tasks)
    add("ASD", tasks)
    remove(2, tasks)
    assert tasks[0]["name"] == "A"
    assert tasks[1]["name"] == "ASD"


def test_view_empty():
    tasks.clear()
    result = view(tasks)
    assert result == []

def test_view():
    tasks.clear()
    add("Shop", tasks)
    add("Clean", tasks)
    result = view(tasks)
    assert result == [{'id': 1, 'name': 'Shop'}, {'id': 2, 'name': 'Clean'}]
