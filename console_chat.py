import os
import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion, AzureChatCompletion
from semantic_kernel import PromptTemplateConfig, PromptTemplate, SemanticFunctionConfig

# Create Semantic kernel builder
kernel = sk.Kernel()
deployment, api_key, endpoint = sk.azure_openai_settings_from_dot_env()
kernel.add_chat_service("my_console_chat", AzureChatCompletion(deployment, endpoint, api_key)) #2 adding AI service

# Create a prompt template
# A) Create a template B) Create a prompt config (config.json can be used) C) Create a prompt template object

template = """{{$input}} Convert the text to an SQL query."""

prompt_config = PromptTemplateConfig.from_completion_parameters(
    max_tokens=2000, temperature=0.7, top_p=0.4
)

prompt_template = PromptTemplate(
    template, kernel.prompt_template_engine, prompt_config
)

# Create a Semantic Function
function_config = SemanticFunctionConfig(prompt_config, prompt_template)
chat_function = kernel.register_semantic_function(skill_name="OrchestratorPlugin", function_name="GetSummary", function_config=function_config)

# Interactive Chat
while True:
    try:
        # Run the prompt
        console_user_input = input("Enter the text to convert to SQL query: ")
        summary = chat_function(console_user_input)
        print(summary)
        if console_user_input == "exit":
            print("Bye!")
            break

    except KeyboardInterrupt:
        print("Bye!")
        break

