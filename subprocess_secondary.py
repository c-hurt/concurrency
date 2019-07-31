import subprocess

# silencing output
try:
    proc_a = subprocess.run(
        'echo $HOME',
        shell=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
except subprocess.CalledProcessError as error:
    print(error)
else:
    print(f'process return code: {proc_a.returncode}')
    print(f'process stdout: {proc_a.stdout}')
    print(f'process stderr: {proc_a.stderr}')

