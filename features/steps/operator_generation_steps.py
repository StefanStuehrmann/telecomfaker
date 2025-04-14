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

@given('I need predictable test data across multiple test runs')
def step_impl(context):
    # Initialize context data dictionary if needed
    if not hasattr(context, 'data'):
        context.data = {}
    
    # Store the seed we'll use for reproducibility
    context.seed_value = 42
    
    # Create our first faker instance with a descriptive name
    context.faker_first_run = TelecomFaker()

@when('I use the same seed value for each test run')
def step_impl(context):
    # Set the seed on the first faker
    context.faker_first_run.set_seed(context.seed_value)
    
    # Generate the first operator
    context.operator_first_run = context.faker_first_run.generate_operator()
    
    # Create a second faker instance to simulate a different test run
    context.faker_second_run = TelecomFaker()
    context.faker_second_run.set_seed(context.seed_value)
    
    # Generate the second operator
    context.operator_second_run = context.faker_second_run.generate_operator()

@then('I should get identical operator data each time')
def step_impl(context):
    # Verify both operators are identical
    assert_that(context.operator_first_run, equal_to(context.operator_second_run))
    
    # Generate another operator with the first faker and verify it's different
    # This ensures the seed is working correctly and not just returning the same value always
    context.operator_next = context.faker_first_run.generate_operator()
    assert_that(context.operator_first_run, is_not(equal_to(context.operator_next)))

@then('I can rely on this consistency for automated testing')
def step_impl(context):
    # Create a third faker instance with the same seed
    context.faker_verification = TelecomFaker()
    context.faker_verification.set_seed(context.seed_value)
    
    # Generate an operator and verify it matches the first one
    context.operator_verification = context.faker_verification.generate_operator()
    assert_that(context.operator_verification, equal_to(context.operator_first_run))
    
    # This demonstrates that the seed provides consistent results
    # across different instances, which is essential for automated testing
