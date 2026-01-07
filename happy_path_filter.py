def extract_happy_path(gherkin_text):
    scenarios = gherkin_text.split("Scenario:")
    happy_scenarios = []

    for scenario in scenarios:
        if "redirected to dashboard" in scenario:
            happy_scenarios.append("Scenario:" + scenario)

    return happy_scenarios


if __name__ == "__main__":
    from llm_generator import generate_gherkin

    gherkin = generate_gherkin("")
    happy = extract_happy_path(gherkin)

    for s in happy:
        print(s)
