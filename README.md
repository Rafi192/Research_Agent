# Research_Agent

### Agentic AI Design Patterns
1. Reflection<br>
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

2. Tool Use: <br>
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

3. Planning <br>

Instead of reacting step by step, the agent first decomposes a complex a goal into a structured plan of subtasks, then executes them. Sometimes reordering or replanning in the mid-way if something fails. 

- There are two main main process in planning. 
a. Plan and then execute : make a full plan upfront and then run it. <br>

for example ,
 <br>

<pre>
user input: ""Write a market research report on EV companies."
                              │
                              ▼
               ┌──────────────────────────────────┐
               │           PLANNER LLM            │
               │  1. Identify top 5 EV companies  │
               │  2. Search financials for each   │
               │  3. Search recent news for each  │
               │  4. Compare and contrast         │
               │  5. Write final report           │
               └──────────────────────────────────┘
                              │
                              ▼
                     EXECUTOR runs each step
                     in sequence (or parallel)
                              │
                              ▼
                        Final output  

</pre>

b. Dynamic Replanning - Plan , Execute step 1, evaluate, replan if needed <br>

<pre>
               Plan: [Search → Summarize → Report] <br>
                           │
            Execute: Search → "No results found for the specific query!" <br>
                           │
            Replan:  "Broaden the search query and try Wikipedia instead" <br>
                           │
            Execute: Wikipedia → Results found <br>
                           │
               Continue: Summarize → Report <br>

</pre>



### Real Example - Trip planning agent

<pre>
Goal : "plan a 5 day trip to japan for 2 people, my budget is under $3000"

Planner produces: 
   Task 1: Search flights Torronto -> Narita, Tokyo
   Task 2: Search hotels in tokyo - 2 people, 3 nights
   Task 3: Serach hotels in kyoto -> 2 nights
   Task 4: Find top attractions for each city including best foods
   Task 5: Estimate daily food budget
   Task 6: Check if total fits under $3000
   Task 7: If over budget, find cheaper alternatives
   Task 8: Write Travel plan 

</pre>

### when should we use planning?
-->  Complex multi-step goals, tasks with dependencies, scenarios where order of execution matters, or where failures need graceful replanning.



