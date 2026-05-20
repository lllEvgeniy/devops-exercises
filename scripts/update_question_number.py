"""
Meant to be used like this:

python scripts/update_question_number.py

Updates only the numeric total in the :bar_chart: line (works for any language).
"""
import pathlib
import re

from scripts.question_utils import get_challenges_count, get_question_list

p = pathlib.Path(__file__).parent.parent.joinpath("README.md")
text = p.read_text(encoding="utf-8")
question_list = get_question_list(text)
question_count = len(question_list)
total_count = question_count + get_challenges_count()
print(question_count)
print(get_challenges_count())
print(total_count)

lines = text.splitlines(keepends=True)
count_re = re.compile(r"\*\*\d+\*\*")
for i, line in enumerate(lines):
    if line.startswith(":bar_chart:"):
        lines[i] = count_re.sub(f"**{total_count}**", line, count=1)
        break

p.write_text("".join(lines), encoding="utf-8", newline="\n")
