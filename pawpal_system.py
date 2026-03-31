from dataclasses import dataclass, field
from datetime import date
from typing import List, Optional


@dataclass
class Task:
    description: str
    time: str
    frequency: str
    pet_name: str
    date: date
    completed: bool = False

    def mark_complete(self) -> None:
        pass

    def is_recurring(self) -> bool:
        pass


@dataclass
class Pet:
    name: str
    species: str
    age: int
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        pass

    def get_tasks(self) -> List[Task]:
        pass

    def get_incomplete_tasks(self) -> List[Task]:
        pass


@dataclass
class Owner:
    name: str
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        pass

    def get_pet_by_name(self, name: str) -> Optional[Pet]:
        pass

    def get_all_tasks(self) -> List[Task]:
        pass


class Scheduler:
    def __init__(self, owner: Owner):
        self.owner = owner

    def get_todays_tasks(self) -> List[Task]:
        pass

    def sort_by_time(self, tasks: List[Task]) -> List[Task]:
        pass

    def filter_tasks(
        self,
        completed: Optional[bool] = None,
        pet_name: Optional[str] = None
    ) -> List[Task]:
        pass

    def detect_conflicts(self, tasks: List[Task]) -> List[str]:
        pass

    def mark_task_complete(self, task: Task) -> None:
        pass

    def create_next_recurring_task(self, task: Task) -> Optional[Task]:
        pass