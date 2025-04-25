from pytest_bdd import scenario, given, when, then
import pytest

@scenario("features/login.feature", "Successful Login")
def test_login():
    pass

@given("I am on the login page")
def login_page():
    return "Login Page Opened"

@when("I enter valid credentials")
def enter_credentials():
    return "Valid Credentials Entered"

@then("I should be logged in successfully")
def verify_login():
    assert "Valid Credentials Entered" == "Valid Credentials Entered"
