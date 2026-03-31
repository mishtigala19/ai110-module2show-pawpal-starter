# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

My initial UML design included four main classes: Owner, Pet, Task, and Scheduler.

The Owner class is responsible for managing the overall system from the user’s side. It stores the owner’s name and a collection of pets, and it provides methods to add pets and access all pets in the system.

The Pet class represents an individual pet. It stores information such as the pet’s name, species, age, and the list of tasks assigned to that pet. Its main responsibility is to keep track of pet-specific care activities like feedings, walks, medications, and appointments.

The Task class represents a single scheduled activity. It stores attributes such as a description, scheduled time, frequency, due date, pet name, and completion status. Its responsibility is to model one care action clearly so it can be sorted, filtered, completed, and reused for recurring schedules.

The Scheduler class acts as the system’s logic layer. Its responsibility is to gather tasks across pets, sort them by time, filter them by status or pet, detect scheduling conflicts, and support recurring task behavior. I separated this class from Owner and Pet so that the scheduling logic would stay organized and easier to test.

**b. Design changes**

During implementation, I made a design change by keeping the scheduling logic inside the Scheduler class instead of spreading it across the Owner and Pet classes. Initially, I considered putting more logic inside the Owner class, but that made the design less clear.

Separating the Scheduler made the system more modular and easier to test. It also made it easier to organize features like sorting, filtering, conflict detection, and recurring tasks.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

The scheduler considers task time, completion status, and which pet a task belongs to. Time is the most important constraint because tasks need to be shown in chronological order.

I decided that time matters most because the main goal of the system is to help the owner understand what needs to be done and when. Filtering by pet and completion status is also useful but comes after time-based organization.

**b. Tradeoffs**

One tradeoff my scheduler makes is that it only detects conflicts when two tasks have the exact same scheduled time. It does not handle overlapping durations.

This tradeoff is reasonable for this project because the system uses simple time-based scheduling and keeps the implementation easier to understand and test.

---

## 3. AI Collaboration

**a. How you used AI**

I used AI tools for brainstorming the system design, generating class structures, implementing methods, and creating test cases. AI was especially helpful in organizing the system and deciding how different classes should interact.

The most helpful prompts were specific ones, such as asking how to sort tasks by time, how to implement recurring task logic, and how to structure the scheduler.

**b. Judgment and verification**

One moment where I did not accept an AI suggestion directly was when deciding where to place the scheduling logic. Instead of placing too much logic inside the Owner class, I kept it in a separate Scheduler class to keep the design clean and modular.

I verified AI suggestions by running the program, checking terminal outputs, and ensuring that all pytest tests passed before accepting the solution.

---

## 4. Testing and Verification

**a. What you tested**

I tested task completion, task addition, sorting by time, recurring task creation, and conflict detection.

These tests were important because they verify the core functionality of the system and ensure that the scheduler behaves correctly.

**b. Confidence**

I am highly confident that my scheduler works correctly because all tests passed successfully.

If I had more time, I would test edge cases such as invalid time formats, empty task lists, and more advanced scheduling conflicts involving overlapping durations.

---

## 5. Reflection

**a. What went well**

The part I am most satisfied with is the scheduling logic. Sorting, filtering, and conflict detection all worked correctly and produced clear and readable output.

**b. What you would improve**

If I had another iteration, I would improve the system by adding support for task durations and more advanced conflict detection. I would also improve the user interface for better visualization of schedules.

**c. Key takeaway**

One important thing I learned is that separating data structures from logic makes systems easier to design, test, and maintain. I also learned that AI is a powerful tool for speeding up development, but it is important to verify and refine its suggestions.