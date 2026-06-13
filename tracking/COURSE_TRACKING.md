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
- Lesson 09 completed: improved argument parsing so inputs like `please count hello world` work.
- Lesson 10 completed: added simple planner for deciding tool, command, or fallback.
- Lesson 11 completed: moved planner logic into `src/planner.py`.
- Lesson 12 completed: moved tool execution into `src/executor.py`.
- Lesson 13 completed: separated plan -> execute -> respond flow.
- Lesson 14 completed: moved action execution into executor.
- Lesson 15 completed: moved constants into `src/config.py`.
- Lesson 16 completed: moved tool registry into `src/tool_registry.py`.
- Lesson 17 completed: moved response logic into `src/responder.py`.
- Lesson 18 completed: added basic `Agent` class.
- Lesson 19 completed: moved fallback response into `Agent` class.
- Lesson 20 completed: moved memory access into `Agent` class.
- Lesson 21 completed: moved exit handling into `Agent` class.
- Lesson 22 completed: removed unused helper functions and cleaned `.gitignore`.

## Current Structure

```text
src/config.py         = constants and settings
src/tool_registry.py  = tool definitions and metadata
src/tools.py          = tool functions
src/planner.py        = intent and planning logic
src/executor.py       = action and tool execution
src/responder.py      = response logic
src/agent.py          = Agent state and behavior
src/basic_agent.py    = main loop
```

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
| 2026-06-14 | Completed | Lesson 09: improved tool argument parsing for flexible inputs. |
| 2026-06-14 | Completed | Lesson 10: added simple planner. |
| 2026-06-14 | Completed | Lesson 11: moved planner into separate module. |
| 2026-06-14 | Completed | Lesson 12: moved tool execution into executor. |
| 2026-06-14 | Completed | Lesson 13: separated plan, execute, and respond flow. |
| 2026-06-14 | Completed | Lesson 14: moved action execution into executor. |
| 2026-06-14 | Completed | Lesson 15: moved constants into config. |
| 2026-06-14 | Completed | Lesson 16: moved tool registry into separate module. |
| 2026-06-14 | Completed | Lesson 17: moved response logic into responder. |
| 2026-06-14 | Completed | Lesson 18: added Agent class. |
| 2026-06-14 | Completed | Lesson 19: moved fallback response into Agent class. |
| 2026-06-14 | Completed | Lesson 20: moved memory access into Agent class. |
| 2026-06-14 | Completed | Lesson 21: moved exit handling into Agent class. |
| 2026-06-14 | Completed | Lesson 22: removed unused helper functions and updated `.gitignore`. |

## Next Action

- Start Lesson 23: review final structure and decide whether to merge `lesson-01-basic-agent` into `main`.
- Keep coding fast; commit only after a meaningful milestone.
