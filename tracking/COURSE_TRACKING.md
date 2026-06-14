# Course Tracking

Repository: `arifariofficial/agent-scratch`

Purpose: keep course progress, notes, completed steps, and next actions in GitHub so ChatGPT can inspect and update it later.

## Current Status

- Current branch: `lesson-02-llm-agent`
- Base branch: `main`
- Learning mode: code first, Git/GitHub checkpoint only after meaningful milestones.
- Lesson 01 branch: completed and merged into `main`.
- Lesson 02 status: active, major milestone completed.
- Current milestone: BasicAgent is connected to Azure AI Foundry OpenAI-compatible endpoint and returns real model responses.
- Authentication mode: API key from `.env`, not Managed Identity.
- Endpoint style: Azure AI Foundry project OpenAI-compatible endpoint, e.g. `/openai/v1` with `api-version` passed via OpenAI client `default_query`.

## Completed Lesson 01: Basic Agent From Scratch

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
- Lesson 23 completed: reviewed final structure, resolved tracking conflict, and merged `lesson-01-basic-agent` into `main`.

## Completed Lesson 02 Milestones: LLM Agent

- Created `src/llm_client.py`.
- Connected fallback responses through an LLM client instead of static echo response.
- Added `LLMClient` class.
- Moved model/provider settings into `src/config.py`.
- Added `src/prompt_builder.py` for clean prompt/message construction.
- Switched from prompt string to chat-style message list.
- Added recent user conversation history into LLM messages.
- Fixed duplicate user message bug in prompt history.
- Added `.env` loading with `python-dotenv`.
- Added `.env.example` without secrets.
- Added `requirements.txt`.
- Configured Azure AI Foundry OpenAI-compatible endpoint.
- Switched to API key authentication from `.env`.
- Verified real model response from Foundry endpoint.
- Added basic LLM client error handling so provider errors return clean strings instead of crashing the app.

## Current Structure

```text
.env.example          = example environment variables, no real secrets
requirements.txt      = Python dependencies
src/config.py         = constants and environment settings
src/tool_registry.py  = tool definitions and metadata
src/tools.py          = tool functions
src/planner.py        = intent and planning logic
src/executor.py       = action and tool execution
src/prompt_builder.py = builds messages for LLM calls
src/llm_client.py     = wraps Azure AI Foundry OpenAI-compatible model call
src/responder.py      = response logic, connects planner output to LLM fallback
src/agent.py          = Agent state and behavior
src/basic_agent.py    = main loop
```

## Environment Variables

Real `.env` file is local-only and must not be committed.

Expected variables:

```env
AZURE_OPENAI_ENDPOINT=https://your-foundry-project.services.ai.azure.com/openai/v1
AZURE_OPENAI_API_KEY=your-api-key-here
AZURE_OPENAI_DEPLOYMENT_NAME=gpt-5.4-mini
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
| 2026-06-14 | Completed | Lesson 23: merged Lesson 01 branch into `main`. |
| 2026-06-14 | Completed | Lesson 02 LLM milestone: connected agent to Azure AI Foundry endpoint with real response. |
| 2026-06-14 | Completed | Lesson 02 cleanup: added `.env.example`, `requirements.txt`, and LLM error handling. |

## Next Action

- Pull the latest tracking commit locally on `lesson-02-llm-agent`.
- Continue Lesson 02 cleanup or start next milestone: tool-aware LLM planning / real agent reasoning loop.
- Keep coding fast; update GitHub tracking only after major milestones.
