from behave import given, when, then
from telecomfaker import TelecomFaker
from telecomfaker.providers import DataProvider
from hamcrest import assert_that, is_not, none, contains_string, greater_than, has_length

@given('I have installed the TelecomFaker package')
def step_impl(context):
    # This is a placeholder step - we're already importing the package
    # so we know it's available
    pass

@when('I need to quickly generate telecom test data')
def step_impl(context):
    # Create a TelecomFaker instance with default settings
    context.faker = TelecomFaker()
    assert context.faker is not None

@then('I should be able to use TelecomFaker without any configuration')
def step_impl(context):
    # Verify the data source is of the correct type (using default)
    assert hasattr(context.faker, 'data_provider')
    assert_that(context.faker.data_provider.__class__.__name__, 
                contains_string('LocalJsonProvider'))

@then('it should provide realistic operator information out of the box')
def step_impl(context):
    # Verify that the data provider has loaded operators
    data = context.faker.data_provider.get_data()
    assert_that(data, is_not(none()))
    assert_that(data.get('operators', []), has_length(greater_than(0)))
    
    # Verify we can generate an operator
    operator = context.faker.generate_operator()
    assert_that(operator, is_not(none()))

@given('I am working in an environment with restricted network access')
def step_impl(context):
    # Create a custom data provider that simulates network restrictions
    class UnavailableDataProvider(DataProvider):
        def __init__(self):
            # Don't do anything that could fail in __init__
            pass
            
        def get_data(self):
            # Fail when data is requested
            raise FileNotFoundError("Data source is unavailable. Please check your network connection and data source configuration.")
    
    # Create a TelecomFaker instance with our custom provider
    context.faker = TelecomFaker(data_provider=UnavailableDataProvider())

@when('I try to generate telecom operator data')
def step_impl(context):
    try:
        context.data = {}
        context.data['operator'] = context.faker.generate_operator()
        context.data['error'] = None
    except Exception as e:
        context.data = {}
        context.data['error'] = str(e)
        context.data['operator'] = None

@then('I should receive a clear error message if data sources are unavailable')
def step_impl(context):
    assert_that(context.data['error'], is_not(none()))
    # Verify the error message contains useful information
    assert_that(len(context.data['error']), is_not(0))

@then('the error should help me troubleshoot the data source issue')
def step_impl(context):
    assert_that(context.data['error'], contains_string('data source')) 