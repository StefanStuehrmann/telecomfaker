from behave import given, when, then
from telecom_faker import TelecomFaker
from hamcrest import assert_that, equal_to, has_key, is_not, none

@given('the TelecomFaker module is initialized')
def step_impl(context):
    # Initialize the TelecomFaker module without installation
    context.faker = TelecomFaker()
    assert context.faker is not None

@given('the telecom data source is loaded')
def step_impl(context):
    # Verify the data source is loaded (we'll mock this for testing)
    assert hasattr(context.faker, 'data_source')
    assert context.faker.data_source is not None

@when('I request a random telecom operator')
def step_impl(context):
    # Store the result for later assertions
    context.data['operator'] = context.faker.generate_operator()

@then('I should receive valid operator information')
def step_impl(context):
    operator = context.data['operator']
    assert_that(operator, is_not(none()))

@then('the information should include name, country, MCC, and MNC')
def step_impl(context):
    operator = context.data['operator']
    assert_that(operator, has_key('name'))
    assert_that(operator, has_key('country'))
    assert_that(operator, has_key('mcc'))
    assert_that(operator, has_key('mnc'))

@then('the information should include size and MVNO status')
def step_impl(context):
    operator = context.data['operator']
    assert_that(operator, has_key('size'))
    assert_that(operator, has_key('is_mvno'))

@given('I set a random seed of {seed:d}')
def step_impl(context, seed):
    context.faker.set_seed(seed)
    context.data['seed'] = seed

@when('I request a random operator twice')
def step_impl(context):
    # Get two operators with the same seed
    context.data['operator1'] = context.faker.generate_operator()
    context.data['operator2'] = context.faker.generate_operator()

@then('I should receive the same operator information both times')
def step_impl(context):
    # Compare the two operators - they should be identical with the same seed
    assert_that(context.data['operator1'], equal_to(context.data['operator2']))