import json
from semantic_kernel import ContextVariables, Kernel
from semantic_kernel.skill_definition import sk_function
from semantic_kernel.orchestration.sk_context import SKContext

class Orchestrator:
    def __init__(self, kernel: Kernel):
        self._kernel = kernel

    @sk_function(
        description="Routes the request to the appropriate function",
        name="RouteRequest",
    )
    async def route_request(self, context: SKContext) -> str:
        # Save the original user request
        request = context["input"]

        ## FUNCTIONS PIPELINE ##

        # Extract the Stock ticker from the user Input
        extract_ticker_function = self._kernel.skills.get_function("OrchestratorPlugin", "ExtractStockTicker")
        
        # Call the Native plugin to get the stock price
        get_stock_price_function = self._kernel.skills.get_function("StocksReaderPlugin", "GetStocks")
        
        # Call the the semantic function CreateResponse to create the response using Azure OpenAI
        create_response = self._kernel.skills.get_function("OrchestratorPlugin", "CreateResponse")

        # Create the pipeline variables
        pipelineVariables = ContextVariables()
        pipelineVariables["original_input"] = request
        pipelineVariables["input"] = request

        # Run the functions in a pipeline and create the response using Azure OpenAI
        output = await self._kernel.run_async(
            extract_ticker_function,
            get_stock_price_function,
            create_response,
            input_vars=pipelineVariables)

        return output.result

        