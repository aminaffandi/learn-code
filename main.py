import subprocess

# Run the git status command
result = subprocess.run(['python', '--version'], capture_output=True, text=True)

# Check the result
if result.returncode == 0:
    print("Command succeeded:")
    print(result.stdout)
else:
    print("Command failed:")
    print(result.stderr)