from behave import given, when, then
from telecomfaker import TelecomFaker
from hamcrest import assert_that, equal_to, has_key, is_not, none, contains_string

@given('I have access to the TelecomFaker library')
def step_impl(context):
    # Initialize the TelecomFaker
    context.faker = TelecomFaker()
    # Verify it's properly initialized
    assert context.faker is not None
    assert hasattr(context.faker, 'data_provider')
    assert context.faker.data_provider is not None

@when('I need a random telecom operator for my test')
def step_impl(context):
    # Generate and store a random operator
    context.data = {}
    context.data['operator'] = context.faker.generate_operator()

@then('I should receive complete operator information')
def step_impl(context):
    # Verify we got valid data
    operator = context.data['operator']
    assert_that(operator, is_not(none()))

@then('the data should include essential operator identifiers')
def step_impl(context):
    # Check for required identification fields
    operator = context.data['operator']
    assert_that(operator, has_key('name'))
    assert_that(operator, has_key('country'))
    assert_that(operator, has_key('mcc'))
    assert_that(operator, has_key('mnc'))

@then('the data should include operator characteristics')
def step_impl(context):
    # Check for operator characteristics
    operator = context.data['operator']
    assert_that(operator, has_key('size'))
    assert_that(operator, has_key('is_mvno'))

@when('I need data for a specific operator that doesn\'t exist')
def step_impl(context):
    # Try to get a non-existent operator
    try:
        context.data = {}
        # We'll use a clearly non-existent name
        context.data['operator_name'] = "NonExistentOperator"
        context.data['operator'] = context.faker.generate_operator(name=context.data['operator_name'])
        context.data['error'] = None
    except Exception as e:
        context.data['error'] = str(e)

@when('I need operator data from a country that isn\'t available')
def step_impl(context):
    # Try to get an operator from a non-existent country
    try:
        context.data = {}
        # We'll use a clearly non-existent country
        context.data['country'] = "NonExistentCountry"
        context.data['operator'] = context.faker.generate_operator(country=context.data['country'])
        context.data['error'] = None
    except Exception as e:
        context.data['error'] = str(e)

@then('I should receive a helpful error message')
def step_impl(context):
    # Verify we got an error message
    assert_that(context.data['error'], is_not(none()))
    assert_that(len(context.data['error']), is_not(0))

@then('the message should suggest checking the operator name')
def step_impl(context):
    # Verify the error message mentions the operator name
    assert_that(context.data['error'], contains_string(context.data['operator_name']))

@then('the message should suggest checking available countries')
def step_impl(context):
    # Verify the error message mentions the country
    assert_that(context.data['error'], contains_string(context.data['country']))

@when('I need consistent operator data across test runs')
def step_impl(context):
    # Set a seed for reproducible results
    context.seed = 42
    context.faker.set_seed(context.seed)

@then('I should be able to use a seed value')
def step_impl(context):
    # Generate first operator
    context.data['operator1'] = context.faker.generate_operator()
    
    # Reset and use the same seed again
    new_faker = TelecomFaker()
    new_faker.set_seed(context.seed)
    context.data['operator2'] = new_faker.generate_operator()

@then('the generated data should be identical for the same seed')
def step_impl(context):
    # Verify both operators are identical
    assert_that(context.data['operator1'], equal_to(context.data['operator2']))
