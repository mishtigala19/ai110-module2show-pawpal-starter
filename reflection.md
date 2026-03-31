# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

My initial UML design included four main classes: Owner, Pet, Task, and Scheduler.

The Owner class is responsible for managing the overall system from the user’s side. It stores the owner’s name and a collection of pets, and it provides methods to add pets and access all pets in the system.

The Pet class represents an individual pet. It stores information such as the pet’s name, species, age, and the list of tasks assigned to that pet. Its main responsibility is to keep track of pet-specific care activities like feedings, walks, medications, and appointments.

The Task class represents a single scheduled activity. I planned for it to store attributes such as a description, scheduled time, frequency, due date, and completion status. Its responsibility is to model one care action clearly so it can be sorted, filtered, completed, and reused for recurring schedules.

The Scheduler class acts as the system’s logic layer. Its responsibility is to gather tasks across pets, sort them by time, filter them by status or pet, detect scheduling conflicts, and later support recurring task behavior. I separated this class from Owner and Pet so that the scheduling logic would stay organized and easier to test.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
