from tests.resources.base import base_resource
from assertpy import assert_that
import json


def prepare_puppies_query():
    base_resource.BaseResource.query = __query_puppies()


def prepare_create_puppy_mutation(puppy_name, puppy_color, breed_id, first_parent_id, second_parent_id):
    base_resource.BaseResource.query = __create_puppy_mutation(puppy_name, puppy_color, breed_id, first_parent_id, second_parent_id)


def assert_query_puppies_response():
    response = base_resource.BaseResource.response.json()
    assert_that(response['data']['puppies']).extracting('name').contains('Tyke')


def assert_create_puppy_mutation_response(puppy_name):
    response = base_resource.BaseResource.response.json()
    assert_that(json.dumps(response['data']['createPuppy']['name'])).contains(puppy_name)


def __query_puppies():
    return "{ puppies { id name breed { name } parents { name breed { name } puppies { name } } } }"


def __create_puppy_mutation(puppy_name, puppy_color, breed_id, first_parent_id, second_parent_id):
    return f"mutation {{ createPuppy(input: {{ name: {puppy_name}, color: {puppy_color}, breedId: {breed_id}, parentsId: [{first_parent_id}, {second_parent_id}] }}) {{ id name color }} }}"
