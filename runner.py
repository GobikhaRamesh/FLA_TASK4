
import subprocess
import sys
import tempfile
import os


def run_with_timeout(source, timeout=2):
    """
    Executes a trusted Python example with a time limit.
    If the program exceeds the limit, it returns UNKNOWN.
    """

    file_path = None

    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            suffix=".py",
            delete=False,
            encoding="utf-8"
        ) as temp_file:

            temp_file.write(source)
            file_path = temp_file.name

        result = subprocess.run(
            [sys.executable, file_path],
            capture_output=True,
            text=True,
            timeout=timeout
        )

        return {
            "status": "HALTS",
            "output": result.stdout.strip(),
            "error": result.stderr.strip()
        }

    except subprocess.TimeoutExpired:

        return {
            "status": "TIMEOUT / UNKNOWN",
            "output": "",
            "error": "Program exceeded the time limit."
        }

    finally:

        if file_path and os.path.exists(file_path):
            os.remove(file_path)
