# Review Matrix

Build a table with one row per paper and these columns:

1. citation
2. year and venue
3. task
4. data or benchmark
5. metric
6. method summary
7. code available
8. hardware assumptions
9. strongest baseline
10. main gain
11. main weakness
12. reproduction risk
13. relevance to the user's project

Use these buckets:

- `core`: directly competes with or enables the target project
- `adjacent`: useful idea, setup, or evaluation trick
- `discard`: off-task, incomparable, weak evidence, or outdated setup

Use these prompts when extracting:

- What changed relative to the strongest baseline?
- Was the gain measured on the same split and metric?
- Are hardware assumptions hidden in throughput or latency claims?
- Is the method reproducible from the paper alone?
- What would I borrow, and what would I avoid?
