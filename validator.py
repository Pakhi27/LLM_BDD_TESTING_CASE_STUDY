ALLOWED_ACTIONS = [
    "login page",
    "enters",
    "clicks",
    "redirected",
    "error message"
]

def validate_gherkin(gherkin_text):
    for action in ALLOWED_ACTIONS:
        if action in gherkin_text:
            return True
    return False


if __name__ == "__main__":
    from llm_generator import generate_gherkin
    gherkin = generate_gherkin("")
    print("Validation Result:", validate_gherkin(gherkin))
