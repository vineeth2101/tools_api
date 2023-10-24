import pytest
import pdb
import allure

# Initialize the data_dict fixture to manage request data
request_data_dict = {"headers": {}, "params": {}, "cookies": {}}


def pytest_bdd_before_scenario(request, feature, scenario):
    # Clear headers, params, and cookies before each scenario

    request_data_dict["headers"].clear()
    request_data_dict["params"].clear()
    request_data_dict["cookies"].clear()

def pytest_bdd_after_scenario(request, feature, scenario):


    pass

@pytest.fixture(scope="function", autouse=True)
def data_dict():
    return request_data_dict                                 

    
