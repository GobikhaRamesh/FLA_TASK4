
from loopcheck.runner import run_with_timeout


def test_terminating_program():
    result = run_with_timeout("print('Hello')")

    assert result["status"] == "HALTS"
    assert "Hello" in result["output"]


def test_timeout_program():
    result = run_with_timeout(
        "while True:\n    pass",
        timeout=1
    )

    assert result["status"] == "TIMEOUT / UNKNOWN"
