from behave import *
from tests.resources.commons import common_resources


@when('dogophql api is called')
def step_impl(context):
    common_resources.call_dogophql_api()
