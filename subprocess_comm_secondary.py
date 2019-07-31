import subprocess

print('reading')
proc_a = subprocess.Popen(
    ['echo', 'stdout'],
    stdout=subprocess.PIPE
)

stdout = proc_a.communicate()[0].decode('utf-8')

print(stdout)

# subprocess routing stdin
print('writing:')

proc_a = subprocess.Popen(
    ['cat', '-'],
    stdin=subprocess.PIPE
)

# communicating to stdin
proc_a.communicate('input to input'.encode('utf-8'))
