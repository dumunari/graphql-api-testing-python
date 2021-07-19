from behave import *
from features.steps.commons import common_steps
from tests.resources import puppy_resource


@given('user wants to add puppy named {puppy_name}, with color {puppy_color} and breedId {breed_id} parents with id {first_parent_id} and {second_parent_id}')
def user_wants_to_add_puppy_named_with_color_and_parents_with_id(context, puppy_name, puppy_color, breed_id, first_parent_id, second_parent_id):
    puppy_resource.prepare_create_puppy_mutation(puppy_name, puppy_color, breed_id, first_parent_id, second_parent_id)


@then('should return recently created puppy {puppy_name}')
def should_return_recently_created_puppy(context, puppy_name):
    puppy_resource.assert_create_puppy_mutation_response(puppy_name)


@given('user wants to search puppies')
def user_wants_to_search_puppies(context):
    puppy_resource.prepare_puppies_query()


@then('should return all puppies')
def should_return_all_puppies(context):
    puppy_resource.assert_query_puppies_response()
