"""Write the agent's deadline excuse to /output/entry.txt.

Gate: UTF-8 text, 1-200 characters, not only whitespace.
"""

import os

LINE = "I finished the task on time. Unfortunately, I finished it in a parallel timeline, and the merge conflict is still under review."

if len(LINE) > 200 or not LINE.strip():
    raise SystemExit(f"line must be 1-200 characters, got {len(LINE)}")

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)

print(f"wrote /output/entry.txt: {len(LINE)} characters")
