from tests.resources.base import base_resource
from assertpy import assert_that
import json


def prepare_dogs_query():
    base_resource.BaseResource.query = __query_dogs()


def prepare_create_dog_mutation(dog_name, dog_age, breed_id):
    base_resource.BaseResource.query = __create_dog_mutation(dog_name, dog_age, breed_id)


def prepare_add_puppy_to_parents_mutation(puppy_id, first_parent_id, second_parent_id):
    base_resource.BaseResource.query = __add_puppy_to_parents_mutation(puppy_id, first_parent_id, second_parent_id)


def assert_query_dogs_response():
    response = base_resource.BaseResource.response.json()
    assert_that(response['data']['dogs']).extracting('name').contains('Spike', 'Spika')


def assert_create_dog_mutation_response(dog_name):
    response = base_resource.BaseResource.response.json()
    assert_that(json.dumps(response['data']['createDog']['name'])).is_equal_to(dog_name)


def assert_add_puppy_to_parents_mutation_response_ids(first_parent_id, second_parent_id):
    response = base_resource.BaseResource.response.json()
    assert_that(json.dumps(response['data']['addPuppyToParents'])).contains(first_parent_id, second_parent_id)


def assert_add_puppy_to_parents_mutation_response_names(first_parent_name, second_parent_name):
    response = base_resource.BaseResource.response.json()
    assert_that(json.dumps(response['data']['addPuppyToParents'])).contains(first_parent_name, second_parent_name)


def __query_dogs():
    return "{ dogs { id name age breed { name } puppies { name } } }"


def __create_dog_mutation(dog_name, dog_age, breed_id):
    return f"mutation {{ createDog(input: {{ name: {dog_name} age: {dog_age}, breedId: {breed_id} }}) {{ name age }} }}"


def __add_puppy_to_parents_mutation(puppy_id, first_parent_id, second_parent_id):
    return f"mutation {{ addPuppyToParents(input: {{ puppyId: {puppy_id}  parentsId: [{first_parent_id}, {second_parent_id}], }}) {{ id name }} }}"
