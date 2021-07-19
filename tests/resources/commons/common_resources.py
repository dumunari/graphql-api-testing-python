from tests.resources.base import base_resource
import requests
import config as config


def call_dogophql_api():
    base_resource.BaseResource.response = requests.post(config.DOGOPHQL_URI + config.DOGOPHQL_PATH,
                                                        json={'query': base_resource.BaseResource.query})
