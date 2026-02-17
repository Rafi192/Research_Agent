# Research_Agent

Agentic AI Design Patterns
1. Reflection
The core idea: The agent critiques and improves its own output before returning it to the user. Instead of a single LLM pass, it runs multiple passes where one "voice" generates and another "voice" evaluates.
Analogy: Like a writer who drafts an essay, then rereads it as a critic, then revises based on their own critique.

```text
User: "Write me a Python function to reverse a linked list"
         │
         ▼
┌─────────────────────┐
│   GENERATOR PASS    │  → Produces first draft of the function
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│   CRITIC PASS       │  → "This doesn't handle empty lists.
│                     │     Edge cases are missing. No docstring."
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│   REVISION PASS     │  → Fixes the issues the critic flagged
└────────┬────────────┘
         │
         ▼
    Final Output
```

<pre>
User: "Write me a Python function to reverse a linked list"
         │
         ▼
┌─────────────────────┐
│   GENERATOR PASS    │  → Produces first draft of the function
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│   CRITIC PASS       │  → "This doesn't handle empty lists.
│                     │     Edge cases are missing. No docstring."
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│   REVISION PASS     │  → Fixes the issues the critic flagged
└────────┬────────────┘
         │
         ▼
    Final Output
</pre>
