# Course Tracking

Repository: `arifariofficial/agent-scratch`

Purpose: keep course progress, notes, completed steps, and next actions in GitHub so ChatGPT can inspect and update it later.

## Current Status

- Started course tracking.
- GitHub access confirmed.
- Tracking file created.
- Current working branch: `lesson-01-basic-agent`.
- Lesson 01 focus: build a basic agent from scratch.
- Basic input echo agent created in `src/basic_agent.py`.
- Lesson branch pushed to GitHub.
- Learning pace rule updated: do not stop for Git after every tiny change.
- Lesson 01 milestone completed: loop, exit command, simple decision logic, and conversation history.
- Lesson 02 milestone completed: cleaner structure with helper functions, command handler, fallback response, agent name/personality, and welcome message.

## Branch Workflow

- `main` stays clean and stable.
- Learning work happens in lesson branches.
- Current branch: `lesson-01-basic-agent`.
- Merge back to `main` only after the lesson works.

## Git Habit

- Do not commit after every small edit.
- Commit after a meaningful milestone works.
- During active learning, prioritize understanding and coding flow.
- Use Git checkpoints when a lesson step is stable, not after every command.

## Lesson 01: Basic Agent

Implemented in `src/basic_agent.py`:

- Continuous input loop.
- Exit command support: `exit`, `quit`, `bye`.
- Simple command handling: `help`, `time`, `history`.
- Conversation history stored in memory.
- Milestone commit pushed from `lesson-01-basic-agent`.

## Lesson 02: Clean Agent Structure

Implemented in `src/basic_agent.py`:

- `clean_input()` helper.
- `should_exit()` helper.
- `handle_command()` command handler.
- `create_fallback_response()` fallback response function.
- `get_agent_response()` as the main response router.
- `AGENT_NAME` and `AGENT_PERSONALITY` constants.
- Welcome message on startup.
- Milestone commit pushed from `lesson-01-basic-agent`.

## Progress Log

| Date | Status | Notes |
|---|---|---|
| 2026-06-13 | Started | Created initial tracking file in GitHub. |
| 2026-06-13 | In progress | Switched to `lesson-01-basic-agent` branch for Lesson 01. |
| 2026-06-13 | Done | Created and pushed `src/basic_agent.py`, a basic input echo agent. |
| 2026-06-13 | Updated | Adjusted learning workflow: less frequent Git checkpoints, faster coding flow. |
| 2026-06-13 | Done | Completed Lesson 01 milestone: loop, commands, and memory. |
| 2026-06-13 | Done | Completed Lesson 02 milestone: clean helper functions and command handler structure. |

## Next Action

- Start Lesson 03: add a simple real tool function.
- Goal: understand how agents use tools by adding a local Python tool before calling any LLM.
- Continue coding first; Git checkpoint only after the next meaningful milestone works.
