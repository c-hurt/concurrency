import subprocess

print('opening new process:')

proc_a = subprocess.Popen(
    ['cat', '-'],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE
)

