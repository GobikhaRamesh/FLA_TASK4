
EXAMPLES = {

    "countdown": """
i = 5

while i > 0:
    print(i)
    i -= 1

print("Finished")
""",

    "unchanged_condition": """
i = 5

while i > 0:
    print(i)
""",

    "infinite_loop": """
while True:
    print("Running")
""",

    "loop_with_break": """
i = 0

while True:
    i += 1

    if i == 3:
        break

print("Stopped")
"""
}
