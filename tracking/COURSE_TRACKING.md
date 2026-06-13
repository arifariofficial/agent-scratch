# Course Tracking

Repository: `arifariofficial/agent-scratch`

Purpose: keep course progress, notes, completed steps, and next actions in GitHub so ChatGPT can inspect and update it later.

## Current Status

- Working branch: `lesson-01-basic-agent`
- Learning mode: code first, Git checkpoint only after meaningful milestones.
- Lesson 01 completed: basic input loop, exit command, decision logic, simple memory.
- Lesson 02 completed: cleaner structure with helper functions, constants, fallback response, agent name/personality, welcome message.
- Lesson 03 completed: basic tool-style commands for time, word count, and uppercase.
- Lesson 04 completed: cleaner command routing using command constants and helper functions.
- Lesson 05 completed: moved tool functions into `src/tools.py`.
- Lesson 06 completed: added a tool registry.
- Lesson 07 completed: added tool metadata with descriptions and examples.
- Lesson 08 completed: added basic intent parsing and text extraction after command.

## Progress Log

| Date | Status | Notes |
|---|---|---|
| 2026-06-13 | Started | Created initial tracking file in GitHub. |
| 2026-06-13 | Completed | Lesson 01: basic agent loop, commands, and memory. |
| 2026-06-13 | Completed | Lesson 02: refactored agent into clean helper functions and constants. |
| 2026-06-13 | Completed | Lesson 03: added fake tool-calling commands: `time`, `count <text>`, `upper <text>`. |
| 2026-06-13 | Completed | Lesson 04: cleaned command routing with constants and helper functions. |
| 2026-06-13 | Completed | Lesson 05: separated agent brain and tools into `src/basic_agent.py` and `src/tools.py`. |
| 2026-06-13 | Completed | Lesson 06: added `TOOLS` registry for tool lookup. |
| 2026-06-13 | Completed | Lesson 07: added tool metadata: function, description, and example. |
| 2026-06-13 | Completed | Lesson 08: added basic intent parsing and argument extraction. |

## Next Action

- Start Lesson 09: better tool argument parsing, so inputs like `please count hello world` can work.
- Keep coding fast; commit only after a meaningful milestone.
