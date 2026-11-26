import os

SENTENCE = "One star: Earth charges for water, hands out opinions free, and its customer service never answers — yet the street tacos were so good I filed my complaint in salsa instead of ink."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(SENTENCE + "\n")
