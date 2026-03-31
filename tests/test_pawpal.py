from datetime import date, timedelta

from pawpal_system import Owner, Pet, Task, Scheduler


def test_mark_complete_changes_status():
    task = Task(
        description="Morning walk",
        time="08:00",
        frequency="daily",
        pet_name="Mochi",
        date=date.today()
    )

    task.mark_complete()

    assert task.completed is True


def test_add_task_to_pet_increases_count():
    pet = Pet(name="Mochi", species="dog", age=3)

    task = Task(
        description="Breakfast",
        time="07:30",
        frequency="daily",
        pet_name="Mochi",
        date=date.today()
    )

    pet.add_task(task)

    assert len(pet.tasks) == 1


def test_sort_by_time_returns_chronological_order():
    owner = Owner(name="Jordan")
    pet = Pet(name="Mochi", species="dog", age=3)
    owner.add_pet(pet)

    task1 = Task(
        description="Walk",
        time="09:00",
        frequency="daily",
        pet_name="Mochi",
        date=date.today()
    )
    task2 = Task(
        description="Breakfast",
        time="07:30",
        frequency="daily",
        pet_name="Mochi",
        date=date.today()
    )
    task3 = Task(
        description="Medication",
        time="08:00",
        frequency="daily",
        pet_name="Mochi",
        date=date.today()
    )

    scheduler = Scheduler(owner)
    sorted_tasks = scheduler.sort_by_time([task1, task2, task3])

    assert [task.description for task in sorted_tasks] == [
        "Breakfast",
        "Medication",
        "Walk"
    ]


def test_mark_task_complete_creates_next_daily_task():
    owner = Owner(name="Jordan")
    pet = Pet(name="Mochi", species="dog", age=3)
    owner.add_pet(pet)

    today = date.today()
    task = Task(
        description="Morning walk",
        time="08:00",
        frequency="daily",
        pet_name="Mochi",
        date=today
    )
    pet.add_task(task)

    scheduler = Scheduler(owner)
    scheduler.mark_task_complete(task)

    assert task.completed is True
    assert len(pet.tasks) == 2
    assert pet.tasks[1].date == today + timedelta(days=1)
    assert pet.tasks[1].completed is False


def test_detect_conflicts_flags_duplicate_times():
    owner = Owner(name="Jordan")
    pet1 = Pet(name="Mochi", species="dog", age=3)
    pet2 = Pet(name="Luna", species="cat", age=5)
    owner.add_pet(pet1)
    owner.add_pet(pet2)

    today = date.today()
    task1 = Task(
        description="Vet appointment",
        time="09:00",
        frequency="once",
        pet_name="Mochi",
        date=today
    )
    task2 = Task(
        description="Medication",
        time="09:00",
        frequency="weekly",
        pet_name="Luna",
        date=today
    )

    scheduler = Scheduler(owner)
    conflicts = scheduler.detect_conflicts([task1, task2])

    assert len(conflicts) == 1
    assert "09:00" in conflicts[0]