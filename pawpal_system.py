from dataclasses import dataclass, field
from datetime import date, datetime, timedelta
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
        """Mark this task as completed."""
        self.completed = True

    def is_recurring(self) -> bool:
        """Return True if the task repeats daily or weekly."""
        return self.frequency.lower() in ["daily", "weekly"]


@dataclass
class Pet:
    name: str
    species: str
    age: int
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a task to this pet."""
        self.tasks.append(task)

    def get_tasks(self) -> List[Task]:
        """Return all tasks for this pet."""
        return self.tasks

    def get_incomplete_tasks(self) -> List[Task]:
        """Return only incomplete tasks for this pet."""
        return [task for task in self.tasks if not task.completed]


@dataclass
class Owner:
    name: str
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to the owner's pet list."""
        self.pets.append(pet)

    def get_pet_by_name(self, name: str) -> Optional[Pet]:
        """Find and return a pet by name."""
        for pet in self.pets:
            if pet.name.lower() == name.lower():
                return pet
        return None

    def get_all_tasks(self) -> List[Task]:
        """Return all tasks across all pets."""
        all_tasks = []
        for pet in self.pets:
            all_tasks.extend(pet.get_tasks())
        return all_tasks


class Scheduler:
    def __init__(self, owner: Owner):
        self.owner = owner

    def get_todays_tasks(self) -> List[Task]:
        """Return all tasks scheduled for today."""
        today = date.today()
        tasks = [task for task in self.owner.get_all_tasks() if task.date == today]
        return self.sort_by_time(tasks)

    def sort_by_time(self, tasks: List[Task]) -> List[Task]:
        """Return tasks sorted by HH:MM time."""
        return sorted(tasks, key=lambda task: datetime.strptime(task.time, "%H:%M"))

    def filter_tasks(
        self,
        completed: Optional[bool] = None,
        pet_name: Optional[str] = None
    ) -> List[Task]:
        """Filter tasks by completion status and/or pet name."""
        tasks = self.owner.get_all_tasks()

        if completed is not None:
            tasks = [task for task in tasks if task.completed == completed]

        if pet_name is not None:
            tasks = [task for task in tasks if task.pet_name.lower() == pet_name.lower()]

        return self.sort_by_time(tasks)

    def detect_conflicts(self, tasks: List[Task]) -> List[str]:
        """Return warning messages for tasks scheduled at the same date and time."""
        warnings = []
        seen = {}

        for task in tasks:
            key = (task.date, task.time)

            if key in seen:
                other_task = seen[key]
                warning = (
                    f"Conflict: '{task.description}' for {task.pet_name} and "
                    f"'{other_task.description}' for {other_task.pet_name} are both scheduled "
                    f"at {task.time} on {task.date}."
                )
                warnings.append(warning)
            else:
                seen[key] = task

        return warnings

    def mark_task_complete(self, task: Task) -> None:
        """Mark a task complete and create the next recurring task if needed."""
        task.mark_complete()

        next_task = self.create_next_recurring_task(task)
        if next_task is not None:
            pet = self.owner.get_pet_by_name(task.pet_name)
            if pet is not None:
                pet.add_task(next_task)

    def create_next_recurring_task(self, task: Task) -> Optional[Task]:
        """Create the next daily or weekly version of a recurring task."""
        frequency = task.frequency.lower()

        if frequency == "daily":
            next_date = task.date + timedelta(days=1)
        elif frequency == "weekly":
            next_date = task.date + timedelta(weeks=1)
        else:
            return None

        return Task(
            description=task.description,
            time=task.time,
            frequency=task.frequency,
            pet_name=task.pet_name,
            date=next_date,
            completed=False
        )