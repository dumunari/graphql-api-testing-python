from behave import *
from tests.resources import breed_resource
from features.steps.commons import common_steps


@given('user wants to add {breed_name} breed')
def user_wants_to_add_new_breed(context, breed_name):
    breed_resource.prepare_create_breed_mutation(breed_name)


@then('should return recently created breed {breed_name}')
def should_return_recently_created_breed(context, breed_name):
    breed_resource.assert_create_breed_mutation_response(breed_name)


@given('user wants to search breeds')
def user_wants_to_search_breeds(context):
    breed_resource.prepare_breeds_query()


@then('should return all breeds')
def should_return_all_breeds(context):
    breed_resource.assert_query_breeds_response()
