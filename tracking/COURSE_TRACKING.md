# Course Tracking

Repository: `arifariofficial/agent-scratch`

Purpose: keep course progress, notes, completed steps, and next actions in GitHub so ChatGPT can inspect and update it later.

## Current Status

- Current branch: `lesson-06-tool-results`
- Base branch: `main`
- Learning mode: code first, Git/GitHub checkpoint only after meaningful milestones.
- Lesson 01 branch: completed and merged into `main`.
- Lesson 02 status: completed on `lesson-02-llm-agent` and merged into `main`.
- Lesson 03 status: completed on `lesson-03-llm-planner` and merged into `main`.
- Lesson 04 status: completed on `lesson-04-agent-loop` and merged into `main`.
- Lesson 05 status: completed on `lesson-05-memory` and merged into `main`.
- Lesson 06 status: active, main milestone completed.
- Current milestone: tool execution now returns structured result dictionaries, final-answer prompts use formatted tool result details, and the formatter safely handles empty/non-dict results.
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

## Completed Lesson 03 Milestones: LLM Planner

- Created `src/llm_planner.py`.
- Added planner prompt that asks the LLM to return strict JSON actions.
- Connected `src/planner.py` to the real `LLMClient`.
- Kept keyword planner as fallback when the LLM plan is invalid.
- Added tool argument support, e.g. `{"type": "tool", "tool_name": "upper", "args": {"text": "hello"}}`.
- Updated executor to use `action["args"]["text"]` for `count` and `upper` when available.
- Improved planner prompt so `args.text` contains only target text, not instruction words.
- Added plan validation for tool names and required tool arguments.
- Verified working behavior:
  - `count words in this text: one two three four` -> `4`
  - `make this uppercase: hello from ariful` -> `HELLO FROM ARIFUL`
  - `hello normal chat` -> real LLM chat response

## Completed Lesson 04 Milestones: Agent Loop

- Added final-answer message builder in `src/prompt_builder.py`.
- Updated `src/responder.py` so tool results are passed back to the LLM for a human-friendly final answer.
- Tool result is no longer just returned raw in the main path.
- Verified working agent loop:
  - normal chat -> fallback -> real LLM answer
  - count request -> LLM planner -> count tool -> LLM final answer using tool result
  - uppercase request -> LLM planner -> upper tool -> LLM final answer using tool result
  - normal chat after tool calls -> fallback -> real LLM answer
- Removed temporary planner debug output before committing.

## Completed Lesson 05 Milestones: Memory

- Upgraded `Agent` memory from raw user strings to structured messages with `role` and `content`.
- Added `remember_user_message()` and `remember_assistant_message()`.
- Updated the main loop so assistant responses are saved after generation.
- Added `get_recent_history(limit)` for controlled memory retrieval.
- Updated fallback LLM messages to include recent conversation history.
- Verified personal memory:
  - `My name is Ariful` -> assistant acknowledges name
  - `What is my name?` -> assistant answers `Ariful`
- Verified tool-result memory:
  - `count words in this text: one two three four` -> final answer saved
  - `What did you just count?` -> assistant remembers the counted text
- Added `MEMORY_MESSAGE_LIMIT` in `src/config.py`.
- Updated `src/prompt_builder.py` to use the configurable memory limit.

## Completed Lesson 06 Milestones: Tool Results

- Updated `src/executor.py` so tool execution returns structured dictionaries instead of raw values.
- Structured tool results include `tool_name`, `input`, and `output`.
- Updated final-answer prompt wording to use structured tool result details.
- Added `src/tool_result_formatter.py`.
- Formatter converts structured tool results into readable tool metadata for the final-answer prompt.
- Formatter safely handles `None` and non-dict results.
- Verified clean user-facing answers:
  - `count words in this text: one two three four` -> natural answer using output `4`
  - `make this uppercase: hello from ariful` -> `HELLO FROM ARIFUL`

## Current Structure

```text
.env.example              = example environment variables, no real secrets
requirements.txt          = Python dependencies
src/config.py             = constants and environment settings, including memory limit
src/tool_registry.py      = tool definitions and metadata
src/tools.py              = tool functions
src/planner.py            = LLM planner + keyword fallback + validation
src/llm_planner.py        = builds planner messages and parses JSON plans
src/executor.py           = action and structured tool execution
src/tool_result_formatter.py = formats structured tool results for prompts
src/prompt_builder.py     = builds fallback, memory-aware, and final-answer messages for LLM calls
src/llm_client.py         = wraps Azure AI Foundry OpenAI-compatible model call
src/responder.py          = response logic, including final LLM answer after tool execution
src/agent.py              = Agent state, structured memory, and behavior
src/basic_agent.py        = main loop
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
| 2026-06-14 | Completed | Lesson 03 LLM planner milestone: JSON action planning, tool args, validation, and normal chat fallback to real LLM. |
| 2026-06-14 | Completed | Lesson 04 agent loop milestone: tool execution is followed by final LLM answer using the tool result. |
| 2026-06-14 | Completed | Lesson 05 memory milestone: structured user/assistant memory, recent history in fallback prompt, tool-result memory, and configurable memory limit. |
| 2026-06-14 | Completed | Lesson 06 tool result milestone: structured tool result dictionaries, formatted tool metadata for final-answer prompts, and safe formatter handling. |

## Next Action

- Pull the latest tracking commit locally on `lesson-06-tool-results`.
- Review Lesson 06 behavior once, then merge `lesson-06-tool-results` into `main` if clean.
- Next coding direction: add another real tool, improve tool schemas, or add tests.
- Keep coding fast; update GitHub tracking only after major milestones.
