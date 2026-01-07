from transformers import pipeline

def generate_gherkin_with_hf(business_requirement: str) -> str:
    """
    Uses Hugging Face FLAN-T5 model locally (text2text-generation)
    to convert business requirements into BDD Gherkin scenarios.
    """

    print("Using Hugging Face local model: google/flan-t5-base")

    generator = pipeline(
        task="text2text-generation",
        model="google/flan-t5-base"
    )

    prompt = f"""
Convert the following business requirement into BDD Gherkin scenarios.

Rules:
- Use Given-When-Then format
- Generate one positive (happy path) scenario
- Generate one negative scenario

Business Requirement:
{business_requirement}
"""

    result = generator(
        prompt,
        max_new_tokens=300,
        temperature=0.2
    )

    return result[0]["generated_text"]


if __name__ == "__main__":
    requirement = """
    User should be able to login using valid credentials.
    Invalid credentials should show an error message.
    """

    gherkin_output = generate_gherkin_with_hf(requirement)

    print("\n=== GENERATED GHERKIN ===\n")
    print(gherkin_output)
