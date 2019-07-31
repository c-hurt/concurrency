import subprocess

proc_a = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE)
proc_a_stdout = proc_a.stdout.decode('utf-8')

print(f'return code: {proc_a.returncode}')
print(f'{proc_a_stdout}')

# routing subprocess errors
try:
    proc_a = subprocess.run(
        'echo the naming',
        check=True,
        shell=True,
        stdout=subprocess.PIPE
    )
except subprocess.CalledProcessError as error:
    print(error)
else:
    std_out_decoded = proc_a.stdout.decode('utf-8')
    print(f'return code: {proc_a.returncode}')
    print(f'completed bytes: {len(std_out_decoded)}')

# piping stderr
try:
    proc_a = subprocess.run(
        'echo the subprocess is running',
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
except subprocess.CalledProcessError as error:
    print(error)
else:
    proc_a_stdout_dec = proc_a.stdout.decode('utf-8')
    proc_a_stderr_dec = proc_a.stderr.decode('utf-8')

    print(f'process return code: {proc_a.returncode}')
    print(f'process stdout: {proc_a_stdout_dec}')
    print(f'process stdout bytes: {len(proc_a_stdout_dec)}')
    print(f'process stderr: {proc_a_stderr_dec}')
    print(f'process stderr bytes: {len(proc_a_stderr_dec)}')

# merging stderr with stdout
try:
    proc_a = subprocess.run(
        'echo $HOME',
        shell=True,
        stderr=subprocess.STDOUT
    )
except subprocess.CalledProcessError as error:
    print(error)
else:
    stdout_reading = proc_a.stdout.decode('utf-8')
    print(f'stdout: {stdout_reading}')
    print(f'stdout: bytes: {len(stdout_reading)}')