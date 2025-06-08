import subprocess
from datetime import datetime
import os

def run_command(cmd):
    """Run a shell command and print output or error"""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"[ERROR] {cmd} -> {result.stderr.strip()}")
    else:
        print(f"[OK] {cmd} -> {result.stdout.strip()}")

def update_heartbeat_file():
    """Update a file with the current timestamp to trigger a commit"""
    with open("heartbeat.txt", "w") as f:
        f.write(f"Last updated at: {datetime.now()}\n")
    print("[INFO] heartbeat.txt updated.")

def auto_commit():
    """Stage, commit, and push changes"""
    update_heartbeat_file()
    run_command("git add heartbeat.txt")
    run_command(f'git commit -m "Auto-update at {datetime.now()}"')
    run_command("git push origin main")  # Change to your branch name if needed

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))  # Ensure script runs in correct directory
    auto_commit()
