from tests.resources.base import base_resource


def before_scenario(context, scenario):
    base_resource.BaseResource.query = ''
    base_resource.BaseResource.response = ''
