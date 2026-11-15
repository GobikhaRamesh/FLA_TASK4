
import ast


def analyze_code(source):
    """
    Performs basic static analysis of while loops.
    This tool identifies suspicious patterns,
    but does not mathematically prove infinite loops.
    """

    findings = []

    try:
        tree = ast.parse(source)
    except SyntaxError as error:
        return [f"Syntax error: {error}"]

    for node in ast.walk(tree):

        if isinstance(node, ast.While):

            # Check for while True
            if (
                isinstance(node.test, ast.Constant)
                and node.test.value is True
            ):

                has_break = any(
                    isinstance(child, ast.Break)
                    for statement in node.body
                    for child in ast.walk(statement)
                )

                if not has_break:
                    findings.append(
                        f"Line {node.lineno}: "
                        "while True has no visible break."
                    )

            # Check whether condition variables are updated
            if isinstance(node.test, ast.Compare):

                condition_variables = {
                    item.id
                    for item in ast.walk(node.test)
                    if isinstance(item, ast.Name)
                }

                updated_variables = set()

                for statement in node.body:
                    for item in ast.walk(statement):
                        if (
                            isinstance(item, ast.Name)
                            and isinstance(item.ctx, ast.Store)
                        ):
                            updated_variables.add(item.id)

                if (
                    condition_variables
                    and not condition_variables.intersection(
                        updated_variables
                    )
                ):
                    findings.append(
                        f"Line {node.lineno}: "
                        "condition variable may not be updated."
                    )

    if not findings:
        findings.append(
            "No obvious infinite-loop pattern detected."
        )

    return findings
