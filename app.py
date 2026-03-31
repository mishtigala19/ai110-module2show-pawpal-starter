import streamlit as st
from datetime import date

from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="P", layout="centered")

st.title("PawPal+")

st.markdown(
    """
Welcome to the PawPal+ app.

This app now connects the Streamlit interface to the backend logic in `pawpal_system.py`.
You can add pets, assign tasks, and generate a daily schedule using your scheduler.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) and organize them into a clear daily schedule.
"""
    )

with st.expander("What this system does", expanded=True):
    st.markdown(
        """
This system can:
- Represent pet care tasks
- Represent pets and owners
- Build a schedule for the day
- Sort tasks by time
- Filter tasks by pet and completion status
- Detect task conflicts
- Support recurring daily and weekly tasks
"""
    )

# -----------------------------
# Session state setup
# -----------------------------
if "owner" not in st.session_state:
    st.session_state.owner = Owner(name="Jordan")

if "owner_name" not in st.session_state:
    st.session_state.owner_name = "Jordan"

st.divider()

# -----------------------------
# Owner section
# -----------------------------
st.subheader("Owner Information")

owner_name = st.text_input("Owner name", value=st.session_state.owner_name)

if st.button("Update Owner"):
    st.session_state.owner_name = owner_name
    st.session_state.owner = Owner(name=owner_name)
    st.success("Owner updated. If you had pets already, please add them again.")

# -----------------------------
# Add pet section
# -----------------------------
st.subheader("Add a Pet")

pet_name = st.text_input("Pet name")
species = st.selectbox("Species", ["dog", "cat", "other"])
age = st.number_input("Pet age", min_value=0, max_value=30, value=1)

if st.button("Add Pet"):
    if not pet_name.strip():
        st.warning("Please enter a pet name.")
    else:
        existing_pet = st.session_state.owner.get_pet_by_name(pet_name)
        if existing_pet is not None:
            st.warning("A pet with that name already exists.")
        else:
            new_pet = Pet(name=pet_name.strip(), species=species, age=age)
            st.session_state.owner.add_pet(new_pet)
            st.success(f"{pet_name} was added successfully.")

# -----------------------------
# Current pets
# -----------------------------
st.subheader("Current Pets")

if st.session_state.owner.pets:
    pet_table = []
    for pet in st.session_state.owner.pets:
        pet_table.append(
            {
                "Name": pet.name,
                "Species": pet.species,
                "Age": pet.age,
                "Number of Tasks": len(pet.tasks),
            }
        )
    st.table(pet_table)
else:
    st.info("No pets added yet.")

st.divider()

# -----------------------------
# Add task section
# -----------------------------
st.subheader("Add a Task")

if st.session_state.owner.pets:
    pet_options = [pet.name for pet in st.session_state.owner.pets]
    selected_pet_name = st.selectbox("Choose pet", pet_options)
else:
    selected_pet_name = None
    st.info("Add a pet first before adding tasks.")

task_title = st.text_input("Task title", value="Morning walk")
task_time = st.text_input("Task time (HH:MM)", value="08:00")
frequency = st.selectbox("Frequency", ["once", "daily", "weekly"])

if st.button("Add Task"):
    if selected_pet_name is None:
        st.warning("Please add a pet first.")
    elif not task_title.strip():
        st.warning("Please enter a task title.")
    else:
        selected_pet = st.session_state.owner.get_pet_by_name(selected_pet_name)

        if selected_pet is not None:
            new_task = Task(
                description=task_title.strip(),
                time=task_time.strip(),
                frequency=frequency,
                pet_name=selected_pet_name,
                date=date.today(),
            )
            selected_pet.add_task(new_task)
            st.success(f"Task added for {selected_pet_name}.")

# -----------------------------
# Show current tasks
# -----------------------------
st.subheader("Current Tasks")

all_tasks = st.session_state.owner.get_all_tasks()

if all_tasks:
    task_table = []
    for task in all_tasks:
        task_table.append(
            {
                "Pet": task.pet_name,
                "Task": task.description,
                "Time": task.time,
                "Frequency": task.frequency,
                "Date": str(task.date),
                "Completed": task.completed,
            }
        )
    st.table(task_table)
else:
    st.info("No tasks yet. Add one above.")

st.divider()

# -----------------------------
# Build schedule
# -----------------------------
st.subheader("Build Schedule")

st.caption("This uses your backend scheduler logic to generate today's schedule.")

scheduler = Scheduler(st.session_state.owner)

if st.button("Generate Schedule"):
    todays_tasks = scheduler.get_todays_tasks()

    if todays_tasks:
        st.success("Schedule generated successfully.")

        schedule_table = []
        for task in todays_tasks:
            schedule_table.append(
                {
                    "Time": task.time,
                    "Pet": task.pet_name,
                    "Task": task.description,
                    "Frequency": task.frequency,
                    "Completed": task.completed,
                }
            )

        st.markdown("### Today's Schedule")
        st.table(schedule_table)

        conflicts = scheduler.detect_conflicts(todays_tasks)
        if conflicts:
            st.markdown("### Conflict Warnings")
            for conflict in conflicts:
                st.warning(conflict)
        else:
            st.info("No scheduling conflicts found.")
    else:
        st.info("No tasks are scheduled for today.")

# -----------------------------
# Filter tasks
# -----------------------------
st.divider()
st.subheader("Filter Tasks")

if st.session_state.owner.pets:
    filter_pet = st.selectbox(
        "Filter by pet",
        ["All Pets"] + [pet.name for pet in st.session_state.owner.pets]
    )
else:
    filter_pet = "All Pets"

filter_status = st.selectbox(
    "Filter by completion status",
    ["All", "Completed", "Incomplete"]
)

if st.button("Apply Filters"):
    completed_value = None
    pet_value = None

    if filter_status == "Completed":
        completed_value = True
    elif filter_status == "Incomplete":
        completed_value = False

    if filter_pet != "All Pets":
        pet_value = filter_pet

    filtered_tasks = scheduler.filter_tasks(
        completed=completed_value,
        pet_name=pet_value
    )

    if filtered_tasks:
        filtered_table = []
        for task in filtered_tasks:
            filtered_table.append(
                {
                    "Time": task.time,
                    "Pet": task.pet_name,
                    "Task": task.description,
                    "Frequency": task.frequency,
                    "Date": str(task.date),
                    "Completed": task.completed,
                }
            )
        st.table(filtered_table)
    else:
        st.info("No tasks match the selected filters.")