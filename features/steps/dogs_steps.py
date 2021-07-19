from behave import *
from features.steps.common import common_steps
from tests.resources import dog_resource


@given('user wants to add dog named {dog_name}, with age {dog_age} breed id {breed_id}')
def user_wants_to_add_dog_with_age_breed_id(context, dog_name, dog_age, breed_id):
    dog_resource.prepare_create_dog_mutation(dog_name, dog_age, breed_id)


@then('should return recently created dog {dog_name}')
def should_return_recently_created_dog_name(context, dog_name):
    dog_resource.assert_create_dog_mutation_response(dog_name)


@given('user wants to search dogs')
def user_wants_to_search_dogs(context):
    dog_resource.prepare_dogs_query()


@then('should return all dogs')
def should_return_all_dogs(context):
    dog_resource.assert_query_dogs_response()


@given('user wants to add puppy with id {puppy_id} to parents with id {first_parent_id} and {second_parent_id}')
def user_wants_to_add_puppy_with_id_to_parents_with_id(context, puppy_id, first_parent_id, second_parent_id):
    dog_resource.prepare_add_puppy_to_parents_mutation(puppy_id, first_parent_id, second_parent_id)


@then('should return parents id {first_parent_id} and {second_parent_id}')
def should_return_parents_id(context, first_parent_id, second_parent_id):
    dog_resource.assert_add_puppy_to_parents_mutation_response_ids(first_parent_id, second_parent_id)


@then(u'parents name {first_parent_name} and {second_parent_name}')
def and_parents_name(context, first_parent_name, second_parent_name):
    dog_resource.assert_add_puppy_to_parents_mutation_response_names(first_parent_name, second_parent_name)
