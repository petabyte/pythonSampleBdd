from behave import *
from Greet import *


@given('I am {name}')
def step_impl(context, name):
    context.greeting = greet(name=name)


@then('Greeting should be {expected}')
def step_impl(context, expected):
    assert (context.greeting == expected)
