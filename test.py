import re
import subprocess

cpu_stdout = subprocess.run(
    ["wmic", "cpu", "get", "name"], shell=True, capture_output=True
).stdout.decode("utf-8")
print(cpu_stdout)

cpu_name = re.findall(r"^[^Name][\n]*[\w\W]+[^\W]", cpu_stdout, re.MULTILINE)
print(cpu_name)
