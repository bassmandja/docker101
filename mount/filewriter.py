import sys
import os
import subprocess
filename = os.path.abspath(sys.argv[1])
print(f'Writing file to {filename}')
with open(filename, 'w') as output:
    output.write(f'File written to {filename}\n')
sys.stdout.flush()
subprocess.run(f'ls -la {filename}', shell=True)
