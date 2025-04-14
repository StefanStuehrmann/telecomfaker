# This file contains setup and teardown functions for the behave tests

def before_all(context):
    # Setup code that runs before all tests
    pass

def after_all(context):
    # Cleanup code that runs after all tests
    pass

def before_feature(context, feature):
    # Setup code that runs before each feature
    pass

def after_feature(context, feature):
    # Cleanup code that runs after each feature
    pass

def before_scenario(context, scenario):
    # Setup code that runs before each scenario
    # Initialize the data dictionary for storing state between steps
    context.data = {}
    
def after_scenario(context, scenario):
    # Cleanup code that runs after each scenario
    # Clear the data dictionary
    context.data = {}