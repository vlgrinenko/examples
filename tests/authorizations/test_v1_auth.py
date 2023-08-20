import json
import os
import requests
import pytest

BASE_URL = "https://reqres.in"
LOGIN_ENDPOINT = "/api/login"

current_directory = os.path.dirname(os.path.abspath(__file__))
credentials_file_path = os.path.abspath(
    os.path.join(current_directory, "..", "..", "src", "until", "credentials_for_auth.json")
)
with open(credentials_file_path, "r") as credentials_file:
    credentials_data = json.load(credentials_file)


class TestV1Auth:
    @pytest.mark.parametrize(
        "credentials", [credentials_data["valid"]]
    )
    def test_v1_successful_auth(self, credentials):
        response = requests.post(BASE_URL + LOGIN_ENDPOINT, json=credentials)

        assert response.status_code == 200, f"Expected status code 200, get {response.status_code}"
        assert "token" in response.json(), "Token not found"

    @pytest.mark.parametrize("invalid_data", [
        "invalid_user",
        "invalid_password",
        "missing_email",
        "missing_password",
        "missing_both"
    ])
    def test_v1_unsuccessful_auth(self, invalid_data):
        credentials = credentials_data["invalid"][invalid_data]["credentials"]
        expected_error = credentials_data["invalid"][invalid_data]["expected_error"]

        response = requests.post(BASE_URL + LOGIN_ENDPOINT, json=credentials)

        assert response.status_code == 400, f"Expected status code 400, get {response.status_code}"
        data = response.json()
        assert "error" in data, "Error message not found"
        assert data["error"] == expected_error, f"Expected error: {expected_error}, get: {data['error']}"
