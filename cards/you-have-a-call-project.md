---
tags:
- project
- macos
- calendar
- notifications
- accessibility
ledger: []
related: []
confidence: high
created: 2026-09-23 00:00:00+00:00
project_started: 2026-09-23
last_active: 2026-09-23
activity_basis: repository commit
activity_status: current
activity_as_of: 2026-09-23
repository_url: https://github.com/david-wolgemuth/you-have-a-call
repository_visibility: public
card_visibility_basis: public repository README and source
visibility: public
---


# You Have a Call is a macOS meeting alert that deliberately takes focus

`you-have-a-call` is a macOS menu bar application that reads selected calendars
through the system Calendar store. When a non-declined event containing a Meet
or Zoom link starts, it focuses an alert window and repeatedly speaks the
meeting title until the alert is dismissed or snoozed.

The menu bar shows the next meeting and can pause alerts. The application runs
at login and relies on macOS Calendar to synchronize external calendars such as
Google Calendar, avoiding a separate Google OAuth integration.

## Resources

- Repository: [david-wolgemuth/you-have-a-call](https://github.com/david-wolgemuth/you-have-a-call).
- Design notes: `docs/design-options.md` (unavailable in this public edition) in the repository.
