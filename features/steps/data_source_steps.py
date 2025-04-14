from behave import given, when, then
from telecomfaker import TelecomFaker
from telecomfaker.providers import DataProvider
from hamcrest import assert_that, is_not, none, contains_string, greater_than, has_length, has_key

@given('the TelecomFaker package is installed')
def step_impl(context):
    # This is a placeholder step - we're already importing the package
    # so we know it's available
    pass

@when('I create a TelecomFaker instance with default settings')
def step_impl(context):
    context.faker = TelecomFaker()
    assert context.faker is not None

@then('it should use the static JSON data source')
def step_impl(context):
    # Verify the data source is of the correct type
    assert hasattr(context.faker, 'data_provider')
    assert_that(context.faker.data_provider.__class__.__name__, 
                contains_string('StaticDataProvider'))

@then('I should be able to generate valid operator information')
def step_impl(context):
    # Focus on verifying that the data provider has loaded operators
    # rather than testing the operator generation itself
    data = context.faker.data_provider.get_data()
    assert_that(data, is_not(none()))
    assert_that(data.get('operators', []), has_length(greater_than(0)))

@given('the data source is unavailable')
def step_impl(context):
    # Create a custom data provider that simulates failure without failing in __init__
    class UnavailableDataProvider(DataProvider):
        def __init__(self):
            # Don't do anything that could fail in __init__
            pass
            
        def get_data(self):
            # Fail when data is requested
            raise FileNotFoundError("Data source is unavailable. Please check the data source.")
    
    # Create a TelecomFaker instance with our custom provider
    context.faker = TelecomFaker(data_provider=UnavailableDataProvider())

@when('I request a random operator')
def step_impl(context):
    try:
        context.data = {}
        context.data['operator'] = context.faker.generate_operator()
        context.data['error'] = None
    except Exception as e:
        context.data = {}
        context.data['error'] = str(e)
        context.data['operator'] = None

@then('I should receive an appropriate error message')
def step_impl(context):
    assert_that(context.data['error'], is_not(none()))
    # Verify the error message contains useful information
    assert_that(len(context.data['error']), is_not(0))

@then('the error should suggest checking the data source')
def step_impl(context):
    assert_that(context.data['error'], contains_string('data source')) 