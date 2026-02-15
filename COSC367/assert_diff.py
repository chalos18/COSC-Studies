import difflib


def compare_results(result_a: str, result_b: str):
    # Normalize line endings and strip trailing spaces for fair comparison
    lines_a = [line.rstrip() for line in result_a.strip().splitlines()]
    lines_b = [line.rstrip() for line in result_b.strip().splitlines()]

    diff = difflib.unified_diff(
        lines_a, lines_b, fromfile="Result A", tofile="Result B", lineterm=""
    )

    differences = list(diff)
    if not differences:
        print("✅ The two result sets match exactly.")
    else:
        print("❌ Differences found:")
        for line in differences:
            print(line)


# Example usage
result1 = """Actions:
  N,
  N.
Total cost: 10
Actions:
  N,
  N.
Total cost: 10
Actions:
  E,
  E,
  E,
  NE,
  NE.
Total cost: 29
Actions:
  N,
  NE,
  Fuel up,
  SW,
  SE,
  E,
  E,
  E,
  NE.
Total cost: 63
Actions:
  W.
Total cost: 5
Actions:
  W,
  W.
Total cost: 10
Actions:
  SW.
Total cost: 7
Actions:
  E,
  E,
  NE,
  Teleport to (4, 3),
  E,
  E.
Total cost: 37
There is no solution!
Actions:
  E,
  E,
  NE,
  Teleport to (4, 1),
  E,
  E,
  Fuel up,
  W,
  W,
  Teleport to (1, 5),
  E,
  E,
  E,
  SE,
  SE,
  SW,
  W.
Total cost: 113"""

result2 = """Actions:
  N,
  N.
Total cost: 10
Actions:
  N,
  N.
Total cost: 10
Actions:
  E,
  E,
  E,
  NE,
  NE.
Total cost: 29
Actions:
  N,
  NE,
  Fuel up,
  SW,
  SE,
  E,
  E,
  E,
  NE.
Total cost: 63
Actions:
  W.
Total cost: 5
Actions:
  W,
  W.
Total cost: 10
Actions:
  SW.
Total cost: 7
Actions:
  E,
  E,
  NE,
  Teleport to (4, 3),
  E,
  E.
Total cost: 37
There is no solution!
Actions:
  E,
  E,
  NE,
  Teleport to (4, 1),
  E,
  E,
  Fuel up,
  W,
  W,
  Teleport to (1, 5),
  E,
  E,
  E,
  SE,
  SE,
  SW,
  W.
Total cost: 113"""

compare_results(result1, result2)
