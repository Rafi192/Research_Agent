# Research_Agent

### Agentic AI Design Patterns
1. Reflection
The core idea: The agent critiques and improves its own output before returning it to the user. Instead of a single LLM pass, it runs multiple passes where one "voice" generates and another "voice" evaluates.
Analogy: Like a writer who drafts an essay, then rereads it as a critic, then revises based on their own critique.

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


Real example — Code Review Agent:

Pass 1 (Generate): LLM writes a sorting algorithm <br>
Pass 2 (Reflect):  LLM reviews it — "O(n²) complexity, won't scale" <br>
Pass 3 (Revise):   LLM rewrites using merge sort<br>
Pass 4 (Reflect):  "Looks good, edge cases covered"<br>
→ Done

2. Tool Use
The core idea: The LLM cannot browse the internet, run code, or query a database on its own. Tools are external functions the LLM can call by name, get results back from, and reason over. The LLM acts as the brain; tools are its hands. <br>
For example --> : Like a brilliant analyst who can't leave their desk, but can ask assistants to go fetch data, run calculations, and come back with results.

<pre>
User: "What is the current stock price of Apple?"
         │
         ▼
      LLM thinks:
  "I need live data.
   I'll call web_search()"
         │
         ▼
┌─────────────────────┐
│    web_search()     │  → Returns: "AAPL: $224.50 as of today"
└────────┬────────────┘
         │
         ▼
      LLM reasons over
      the result and
      forms a response
         │
         ▼
  "Apple (AAPL) is currently
   trading at $224.50"  


</pre>

The reasearch agent example :

Query: "Summarize the latest research on LLM hallucination"

Step 1 → LLM calls web_search("LLM hallucination 2025 research paper")<br>
Step 2 → LLM calls fetch_url("https://arxiv.org/abs/2504.17550")<br>
Step 3 → LLM calls  summarize_text(the_scraped_content)<br>
Step 4 → LLM calls write_report(all_findings)<br>
→ output done.

The ReAct pattern (Reason + Act) drives this:<br>
Thought:  "I need to find recent papers"<br>
Action:   web_search("LLM hallucination 2025")<br>
Observe:  [search results returned] <br>
Thought:  "I should read this arxiv link" <br>
Action:   fetch_url("https://arxiv.org/abs/2504.17550") <br>
Observe:  [page content returned] <br>
Thought:  "I have enough. I'll write the report now." <br>
Action:   write_report(...)<br>
→ Final Answer