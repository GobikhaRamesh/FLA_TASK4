
from loopcheck.analyzer import analyze_code


def test_detects_while_true():
    code = "while True:\n    print('hello')"

    result = analyze_code(code)

    assert any("while True" in item for item in result)


def test_normal_loop():
    code = "i = 5\nwhile i > 0:\n    i -= 1"

    result = analyze_code(code)

    assert result


def test_invalid_python():
    code = "while"

    result = analyze_code(code)

    assert "Syntax error" in result[0]
