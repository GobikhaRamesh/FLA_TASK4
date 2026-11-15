
from loopcheck.examples import EXAMPLES
from loopcheck.analyzer import analyze_code
from loopcheck.runner import run_with_timeout


def main():

    print("=" * 55)
    print("       LOOPCHECK - INFINITE LOOP DETECTION")
    print("=" * 55)

    for name, source in EXAMPLES.items():

        print(f"\nPROGRAM: {name}")
        print("-" * 55)

        print("\n1. STATIC ANALYSIS")

        findings = analyze_code(source)

        for finding in findings:
            print("   ", finding)

        print("\n2. BOUNDED EXECUTION")

        result = run_with_timeout(source, timeout=2)

        print("   Status:", result["status"])

        if result["output"]:
            print("   Output:", result["output"][:200])

        if result["error"]:
            print("   Details:", result["error"][:200])

    print("\n" + "=" * 55)
    print("Analysis completed.")
    print("=" * 55)


if __name__ == "__main__":
    main()
