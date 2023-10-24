from pytest_bdd import parsers, then, when, given
from requests import Response
from utils.request_helpers import make_request
import os
import pdb
import allure


@given("Add request header to data dict")
def add_valid_tenant_parameter(data_dict):
    data_dict.get("headers")["token"] = os.environ['token']


@when("User request post connection endpoint", target_fixture="response")
def post_connections_request(data_dict):
        return make_request(
        method="GET",
        headers=data_dict.get("headers"),
        endpoint=os.environ["sampleApi"],
    )


@then(
    parsers.parse("User should get {status:d} status code"),
    target_fixture="response_data",
)
def verify_status(status: int, response: Response):
    assert response.status_code == status
    return response.json()
