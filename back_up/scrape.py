import subprocess

def execute_script(script_path):
    try:
        subprocess.run(['python', script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing {script_path}: {e}")

if __name__ == "__main__":
    scripts_to_execute = [
        "gearvn_bp.py",
        "gearvn_cr.py",
        "fpt_bp.py",
        "fpt_cr.py",
        "phucanh_cr.py",
        "brand.py",
        "push.py"
    ]

    for script in scripts_to_execute:
        print(f"Executing {script}...")
        execute_script(script)
        print(f"{script} executed.\n")
