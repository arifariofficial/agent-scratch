# Course Tracking

Repository: `arifariofficial/agent-scratch`

Purpose: keep course progress, notes, completed steps, and next actions in GitHub so ChatGPT can inspect and update it later.

## Current Status

- Main branch: `main`
- Lesson 01 branch: `lesson-01-basic-agent` merged into `main`.
- Next working branch: `lesson-02-llm-agent`
- Learning mode: code first, Git checkpoint only after meaningful milestones.
- Lesson 01 completed: basic local rule-based agent from scratch.
- Lesson 02 goal: connect the agent to an LLM and start turning it into a real LLM-powered agent.

## Completed Lesson 01 Topics

- Basic input loop
- Exit commands
- Conversation memory
- Command routing
- Tool-style functions
- Tool registry
- Tool metadata
- Intent parsing
- Argument extraction
- Planner module
- Executor module
- Responder module
- Config module
- Agent class
- Agent-owned memory access
- Agent-owned fallback response
- Agent-owned exit handling
- `.gitignore` cleanup
- Branch merge into `main`
- Basic merge conflict resolution

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
| 2026-06-14 | Completed | Lesson 23: reviewed final structure and merged `lesson-01-basic-agent` into `main`. |

## Next Action

- Create or switch to branch `lesson-02-llm-agent`.
- Pull latest `main` first because this tracking file was updated directly on GitHub.
- Start Lesson 02: connect the agent to an LLM.
- Keep coding fast; commit only after a meaningful milestone.
