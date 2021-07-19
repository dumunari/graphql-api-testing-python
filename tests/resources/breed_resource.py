from tests.resources.base import base_resource
from assertpy import assert_that
import json


def prepare_breeds_query():
    base_resource.BaseResource.query = __query_breeds()


def prepare_create_breed_mutation(breed_name):
    base_resource.BaseResource.query = __create_breed_mutation(breed_name)


def assert_query_breeds_response():
    response = base_resource.BaseResource.response.json()
    assert_that(response['data']['breeds']).extracting('name').contains('English bulldog')


def assert_create_breed_mutation_response(breed_name):
    response = base_resource.BaseResource.response.json()
    assert_that(json.dumps(response['data']['createBreed']['name'])).is_equal_to(breed_name)


def __query_breeds():
    return "{ breeds { id name } }"


def __create_breed_mutation(breed_name):
    return "mutation {{ createBreed ( input: {{ name: {breed_name} }}) {{ id name }} }}".format(breed_name=breed_name)
