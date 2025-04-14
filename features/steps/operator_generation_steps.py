from behave import given, when, then
from telecomfaker import TelecomFaker
from telecomfaker.models import TelecomOperator
from hamcrest import assert_that, equal_to, has_property, is_not, none, contains_string, instance_of

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
    context.operator = context.faker.generate_operator()

@then('I should receive complete operator information')
def step_impl(context):
    # Verify we got valid data
    assert_that(context.operator, is_not(none()))
    # Verify it's a TelecomOperator instance
    assert_that(context.operator, instance_of(TelecomOperator))

@then('the data should include essential operator identifiers')
def step_impl(context):
    # Check for required identification fields using has_property matcher
    assert_that(context.operator, has_property('name'))
    assert_that(context.operator, has_property('country'))
    assert_that(context.operator, has_property('mcc'))
    assert_that(context.operator, has_property('mnc'))
    
    # Verify the properties have values
    assert_that(context.operator.name, is_not(none()))
    assert_that(context.operator.country, is_not(none()))
    assert_that(context.operator.mcc, is_not(none()))
    assert_that(context.operator.mnc, is_not(none()))

@then('the data should include operator characteristics')
def step_impl(context):
    # Check for operator characteristics
    assert_that(context.operator, has_property('size'))
    assert_that(context.operator, has_property('is_mvno'))
    
    # Verify the size property has a value
    assert_that(context.operator.size, is_not(none()))

@then('I should receive a helpful error message')
def step_impl(context):
    # Verify we got an error message
    assert_that(context.error, is_not(none()))
    assert_that(len(context.error), is_not(0))

@then('the message should suggest checking the operator name')
def step_impl(context):
    # Verify the error message mentions the operator name
    assert_that(context.error, contains_string(context.operator_name))

@then('the message should suggest checking available countries')
def step_impl(context):
    # Verify the error message mentions the country
    assert_that(context.error, contains_string(context.country))

@given('I need predictable test data across multiple test runs')
def step_impl(context):
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
    # Verify both operators are identical by comparing their dict representations
    # This is needed because Pydantic models don't implement __eq__ by default
    assert_that(context.operator_first_run.dict(), equal_to(context.operator_second_run.dict()))
    
    # Generate another operator with the first faker and verify it's different
    context.operator_next = context.faker_first_run.generate_operator()
    assert_that(context.operator_first_run.dict(), is_not(equal_to(context.operator_next.dict())))

@then('I can rely on this consistency for automated testing')
def step_impl(context):
    # Create a third faker instance with the same seed
    context.faker_verification = TelecomFaker()
    context.faker_verification.set_seed(context.seed_value)
    
    # Generate an operator and verify it matches the first one
    context.operator_verification = context.faker_verification.generate_operator()
    assert_that(context.operator_verification.dict(), equal_to(context.operator_first_run.dict()))
    
    # This demonstrates that the seed provides consistent results
    # across different instances, which is essential for automated testing
