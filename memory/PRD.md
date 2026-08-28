# Class Cue — Product Foundation

## Original problem statement
Build the first polished, viewable foundation of Class Cue, a teacher-first productivity workspace that helps a teacher see what is next, prepare, teach, record, and review. The first build includes Dashboard, Calendar, Class Session, Students, Student Profile, and Subjects, with realistic sample data and connected teaching records. It intentionally excludes authentication, AI, external calendar sync, uploads, messaging, payments, and school administration.

## Architecture decisions
- React frontend with a focused workspace shell and four primary navigation destinations.
- FastAPI state endpoints at `/api/state` backed by the existing MongoDB connection.
- A small state document keeps the first prototype easy to extend while preserving relationships between subjects, sessions, lessons, attendance, assignments, grades, students, and notes.
- Dashboard signals use sample records and simple rule-based presentation; no AI or external service is used.
- Frontend uses the design direction in `design_guidelines.json`: Outfit headings, Plus Jakarta Sans body text, warm organic earth tones, spacious hierarchy, and tablet-friendly layouts.

## User personas
- Alex Morgan, a teacher who needs a calm daily command center.
- Teachers, tutors, professors, and independent instructors managing their own classes.

## Core requirements (static)
- Prioritize What's Next, Needs Attention, Student Pulse, Today, Quick Actions, and Today's Progress.
- Provide Calendar day/week/month views and openable sessions.
- Provide session Planning, Attendance, Assignment, and Grades tabs.
- Provide Students search, profile, add/archive/delete actions, and Subjects management.
- Preserve the teacher's workflow and avoid database-style overload.

## What's implemented
- 2026-06-16: Built the Class Cue shell, dashboard cockpit, schedule cards, progress signal, focus list, student pulse, and quick actions.
- 2026-06-16: Added calendar views, session status, lesson planning, attendance with no duplicate session/student records, assignments, and gradebook surfaces.
- 2026-06-16: Added student search/profile, attendance summary, donut visualization, notes, recent grades, subjects, sample data, API persistence, and responsive styling.
- 2026-06-16: Verified production build, preview navigation, session opening, bulk attendance for eight students, and student search at desktop width.

## Prioritized backlog
### P0
- Replace prompt-based add/edit controls with polished modal forms and explicit confirmation dialogs.
- Complete calendar add/edit/reschedule persistence for day and month layouts.

### P1
- Add editable student profile fields and full attendance history rows from stored records.
- Add assignment edit/delete and inline grade save persistence per assignment.
- Add real rule evaluation for all three Student Pulse patterns from attendance and grade history.

### P2
- Add richer lesson status summaries and a compact history view for completed sessions.
- Add import/export for a teacher's workspace without introducing school administration.

## Next tasks
1. Build reusable modal forms for student, subject, class, assignment, and note editing.
2. Finish Calendar day/month visual layouts and rescheduling interactions.
3. Replace hardcoded student pulse copy with calculated signals from stored records.