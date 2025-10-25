# todo-app-2025 - What I Did

I added a new `/remove/<id>` route in `views.py` and a **“remove”** link in the HTML template so that tasks can be deleted directly by their ID.  
I also extended the `Task` model by adding a `priority` column and updated the form and view logic to handle different priority levels (high, medium, low).  
To fix password hashing issues, I switched the method to PBKDF2 for compatibility.

### Why It Matters

This solves the required features in the slide:
- ✅ Added a route to remove tasks (with working front-end and back-end logic).  
- ✅ Implemented optional task priority with basic styling.  
- ✅ Fixed database and hashing errors so the app runs smoothly.  

With these changes, the app now supports creating, checking, removing, and prioritizing tasks, meeting the assignment goals cleanly.
