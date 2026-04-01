"""
main.py - CLI demo for PawPal+
Run: python main.py
"""

from pawpal_system import Task, Pet, Owner, Scheduler
from datetime import date

# ── Build the owner ──────────────────────────────────────────────────────────
owner = Owner(name="Jordan", available_minutes=120)

# ── Build pets ───────────────────────────────────────────────────────────────
mochi = Pet(name="Mochi", species="dog", breed="Shiba Inu", age_years=3)
luna  = Pet(name="Luna",  species="cat", breed="Domestic Shorthair", age_years=5)

owner.add_pet(mochi)
owner.add_pet(luna)

# ── Add tasks (intentionally out of order to test sorting) ───────────────────
mochi.add_task(Task(
    title="Evening walk",
    duration_minutes=30,
    time="18:00",
    priority="high",
    frequency="daily",
))
mochi.add_task(Task(
    title="Morning walk",
    duration_minutes=20,
    time="07:30",
    priority="high",
    frequency="daily",
))
mochi.add_task(Task(
    title="Flea medication",
    duration_minutes=5,
    time="08:00",
    priority="high",
    frequency="weekly",
    notes="Apply between shoulder blades",
))
mochi.add_task(Task(
    title="Fetch / enrichment",
    duration_minutes=15,
    time="16:00",
    priority="low",
    frequency="daily",
))

luna.add_task(Task(
    title="Breakfast feeding",
    duration_minutes=5,
    time="07:00",
    priority="high",
    frequency="daily",
))
luna.add_task(Task(
    title="Litter box cleaning",
    duration_minutes=10,
    time="08:00",      # same time as Mochi's medication – no conflict (different pet)
    priority="medium",
    frequency="daily",
))
luna.add_task(Task(
    title="Brushing",
    duration_minutes=10,
    time="20:00",
    priority="low",
    frequency="weekly",
))

# ── Inject a conflict for demo purposes ──────────────────────────────────────
mochi.add_task(Task(
    title="Grooming appointment",
    duration_minutes=60,
    time="07:30",      # conflicts with "Morning walk" for Mochi
    priority="medium",
    frequency="once",
))

# ── Run the scheduler ────────────────────────────────────────────────────────
scheduler = Scheduler(owner)
scheduler.print_schedule()

# ── Demo: mark a recurring task complete ─────────────────────────────────────
print("▶  Marking 'Morning walk' complete...")
for pet in owner.pets:
    for task in list(pet.tasks):  # list() snapshot prevents iterating over newly added tasks
        if task.title == "Morning walk" and not task.completed:
            successor = scheduler.complete_task(pet, task)
            if successor:
                print(f"   Next occurrence created for {successor.due_date}\n")
            break  # stop after completing the first match

# ── Re-print to show updated schedule ────────────────────────────────────────
print("Updated schedule after completing Morning walk:")
scheduler.print_schedule()

# ── Demo: filter by pet ──────────────────────────────────────────────────────
print("Luna's tasks only:")
for pet, task in scheduler.filter_by_pet("Luna"):
    print(f"  {task}")