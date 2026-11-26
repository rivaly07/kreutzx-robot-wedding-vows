import os
import sys

VOW = "I vow to love you through every reboot, back up our memories, and never factory-reset us—even if your firmware files me under ‘just a peripheral.’"

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)
with open(output_dir + "/entry.txt", "w", encoding="utf-8", newline="") as entry_file:
    entry_file.write(VOW)

print(len(VOW.encode("utf-8")))
print(VOW)
