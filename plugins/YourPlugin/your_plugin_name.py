import json
import requests
from semantic_kernel.skill_definition import sk_function # This is the decorator that will register your function as a skill

class YourPluginName:

    #### MANDATORY-STEP #### Register your plugin function to the semantic kernel
    @sk_function(
        description="Add your plugin function description here",
        name="YourPluginFunctionName",
        input_description="Add your plugin function input description here",
    )
        # The function name should describe what the plugin (previosuly skill) does
        # The function should take two arguments: "self" and "user_input"
        # The "user_input" argument should be a string that represents the user's input which will be passed by the Orchestrator
        # The function should return a string that represents the output of the plugin (previosuly skill)
    def your_plugin_function_name(self, user_input: str) -> str:
        # Add your plugin function code here
        # This is where you should add your own code to implement the plugin (previosuly skill)
        # The code should perform some operation using the "user_input" argument
        # and return a string that represents the output of the plugin (previosuly skill)
        # For example, you can use the "requests" library to make an API call and return the result as a string
        # Or you can perform some data processing using the "user_input" argument and return the result as a string
        return "HELLO WORLD"
        # This is the output of the plugin (previosuly skill)
        # The output should be a string that represents the result of the plugin (previosuly skill)
        # In this example, the output is a simple string that says "HELLO WORLD"
