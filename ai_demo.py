from care_advisor import CareAdvisor


def run_demo():
    advisor = CareAdvisor()

    example_queries = [
        "My dog is vomiting and seems tired.",
        "I forgot to give my cat her medication.",
        "My dog cannot breathe and collapsed.",
        "My rabbit seems bored and needs more exercise.",
    ]

    print("\nPawPal+ AI Care Advisor Demo")
    print("=" * 50)

    for query in example_queries:
        print("\nUser Input:")
        print(query)

        advice = advisor.generate_advice(query)

        print("\nSystem Output:")
        print(advisor.format_advice(advice))
        print("-" * 50)


if __name__ == "__main__":
    run_demo()