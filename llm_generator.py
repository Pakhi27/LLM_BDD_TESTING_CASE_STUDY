def generate_gherkin(requirement_text):
    """
    Simulates LLM converting business requirements to Gherkin scenarios
    """

    gherkin = """
Feature: User Login

Scenario: Successful login with valid credentials
  Given user is on login page
  When user enters valid username and password
  And clicks login button
  Then user should be redirected to dashboard

Scenario: Login fails with invalid credentials
  Given user is on login page
  When user enters invalid username or password
  And clicks login button
  Then error message should be displayed
"""
    return gherkin


if __name__ == "__main__":
    req = """
    User should be able to login using valid credentials.
    Invalid credentials should show error.
    """
    print(generate_gherkin(req))
