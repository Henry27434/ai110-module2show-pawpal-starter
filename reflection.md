# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
    Mirroring real-world roles, my UML design had Task, Pet, Owner, and a Scheduler class.
- What classes did you include, and what responsibilities did you assign to each?
    Task: holds a single care activity with title, duration, priority, frequency,etc.
    Pet: stores pet identity info and owns a list of Task objects; exposes helpers to add, remove, and filter tasks.
    Owner: manages a list of Pet objects and exposes a daily time budget that the scheduler must respect.
    Scheduler: takes an Owner reference and provides sorting, recurring task promotion, and the final build_daily_schedule() method.

**b. Design changes**

- Did your design change during implementation?
    Initially I planned to store tasks directly on the Scheduler as a flat list. Copilot pointed out that this would make it impossible to know which pet a task belonged to.
- If yes, describe at least one change and why you made it.
    I moved task ownership entirely to Pet and had Scheduler delegate retrieval which would then help filter and clean up the code.
---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
    It considers Time budget, Complete status, chronoloigical ordering, and conflict detection
- How did you decide which constraints mattered most?
    Since the situation mentioned a busy pet owner, the reasonable constraint to focus on would be the Time budget.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
    The conflict detection only flags tasks at the exact same time string, not overlapping durations.
- Why is that tradeoff reasonable for this scenario?
    Exact-match is simple to understand and a missed conflict is far less harmful than blocking legitimate tasks.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
    I used Copilot for UML generation and general brainstorming if I got stuck making the UML design
- What kinds of prompts or questions were most helpful?
    Asking it "what edge cases am I missing?" gave insight that I may have missed or more that I did not consider before that I could review.

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
    When implementing build_daily_schedule, Copilot generated a version that sorted entirely by priority 
- How did you evaluate or verify what the AI suggested?
    Since the scenario asks owners when things happen, chronological order is more useful.

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
    mark_complete flag, recurrence successors, add/remove task counts, sort order.
- Why were these tests important?
    Scheduling bugs like tasks silently dropped or wrong order would erode owner trust and make the app seem unreliable and unpredictable

**b. Confidence**

- How confident are you that your scheduler works correctly?
    Mostly confident, as everything seems to be working when reviewed at least for given test cases
- What edge cases would you test next if you had more time?
    Tasks whose combined durations exceed the budget by exactly 1 minute

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?
    The clean separation between pawpal_system.py and app.py.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?
    Replace the exact-time conflict check with duration-aware overlap detection.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
    To always review and test the code that the AI gives, even if it looks promising/trustworthy.
