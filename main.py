from datetime import date

from pawpal_system import Owner, Pet, Task, Scheduler


def print_schedule(tasks):
    print("\nToday's Schedule")
    print("-" * 40)

    if not tasks:
        print("No tasks scheduled for today.")
        return

    for task in tasks:
        status = "Completed" if task.completed else "Pending"
        print(
            f"{task.time} | {task.pet_name} | {task.description} | "
            f"{task.frequency} | {status}"
        )


def main():
    owner = Owner(name="Jordan")

    dog = Pet(name="Mochi", species="dog", age=3)
    cat = Pet(name="Luna", species="cat", age=5)

    owner.add_pet(dog)
    owner.add_pet(cat)

    today = date.today()

    task1 = Task(
        description="Morning walk",
        time="08:00",
        frequency="daily",
        pet_name="Mochi",
        date=today
    )
    task2 = Task(
        description="Breakfast",
        time="07:30",
        frequency="daily",
        pet_name="Mochi",
        date=today
    )
    task3 = Task(
        description="Medication",
        time="09:00",
        frequency="weekly",
        pet_name="Luna",
        date=today
    )
    task4 = Task(
        description="Vet appointment",
        time="09:00",
        frequency="once",
        pet_name="Mochi",
        date=today
    )

    dog.add_task(task1)
    dog.add_task(task2)
    dog.add_task(task4)
    cat.add_task(task3)

    scheduler = Scheduler(owner)

    todays_tasks = scheduler.get_todays_tasks()
    print_schedule(todays_tasks)

    print("\nIncomplete Tasks for Mochi")
    print("-" * 40)
    for task in scheduler.filter_tasks(completed=False, pet_name="Mochi"):
        print(f"{task.time} | {task.description}")

    print("\nConflict Warnings")
    print("-" * 40)
    conflicts = scheduler.detect_conflicts(todays_tasks)
    if conflicts:
        for conflict in conflicts:
            print(conflict)
    else:
        print("No conflicts found.")


if __name__ == "__main__":
    main()