from graph import build_graph


def main():
    print("=" * 55)
    print("       LOCAL AI MULTI-AGENT CODING SYSTEM")
    print("=" * 55)

    task = input("\nEnter your development task: ").strip()

    if not task:
        print("Please enter a task.")
        return

    app = build_graph()

    initial_state = {
        "task": task,
        "plan": "",
        "code": "",
        "review": "",
        "tests": "",
    }

    print("\n[1/4] Planner Agent working...")
    print("[2/4] Developer Agent working...")
    print("[3/4] Reviewer Agent working...")
    print("[4/4] Tester Agent working...")

    result = app.invoke(initial_state)

    sections = [
        ("IMPLEMENTATION PLAN", result["plan"]),
        ("GENERATED CODE", result["code"]),
        ("CODE REVIEW", result["review"]),
        ("TEST CASES", result["tests"]),
    ]

    for title, content in sections:
        print("\n" + "=" * 55)
        print(title)
        print("=" * 55)
        print(content)

    print("\nWorkflow completed.")


if __name__ == "__main__":
    main()