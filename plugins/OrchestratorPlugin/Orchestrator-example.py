import json
from semantic_kernel import ContextVariables, Kernel
from semantic_kernel.skill_definition import sk_function
from semantic_kernel.orchestration.sk_context import SKContext

class Orchestrator:
    
    #### MANDATORY-STEP #### Intialize the Orchestrator with the kernel (passed from the main program)
    def __init__(self, kernel: Kernel):
        self._kernel = kernel

    #### MANDATORY-STEP #### In every orchestrator plugin, you need to have an orchestrator function
    #### This function will orchestrate the execution of the other functions (called Nested Functions)
    @sk_function(
        description="Routes the request to the appropriate function",
        name="RouteRequest",
    )
    async def route_request(self, context: SKContext) -> str:
        # Save the original user input (passed from the main program)
        request = context["input"]
        # Create a context variable to store the user input
        variables = ContextVariables()
        variables["input"] = request


        ## BUILDING THE FUNCTIONS PIPELINE TO CREATE THE RESPONSE ##

        #### MANDATORY-STEP1 #### Get the semantic function under the Orchestrator plugin path "OrchestratorPlugin/YourSemanticFunction"
        your_semantic_function = self._kernel.skills.get_function("OrchestratorPlugin", "YourSemanticFunction")
        
        #### MANDATORY-STEP2 #### Get the native function from the plugin that you want to call e.g. "plugins/YourPlugin"
        your_native_function = self._kernel.skills.get_function("YourPlugin", "YourNativeFunction")
        
        #### MANDATORY-STEP3 #### Get the function that will create the response using Azure OpenAI
        create_response_semantic_function = self._kernel.skills.get_function("OrchestratorPlugin", "CreateResponse")

        #### MANDATORY-STEP #### Store the returned values from the functions in a context variable
        pipelineVariables = ContextVariables()
        pipelineVariables["original_input"] = request
        pipelineVariables["input"] = request

        # Run the functions in a pipeline and create the response using OpenAI
        output = await self._kernel.run_async(
            your_semantic_function,
            your_native_function,
            create_response_semantic_function,
            input_vars=pipelineVariables)

        return output.result

        