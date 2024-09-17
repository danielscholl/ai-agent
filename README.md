# AI Agent

An AI agent application that interacts with Azure OpenAI services.

## Prerequisites

- Python 3.12+
- [Poetry](https://python-poetry.org/docs/#installation)
- Azure OpenAI account and endpoint

## Setup

1. Clone the repository:
   ```
   git clone [your-repo-url]
   cd ai-agent
   ```

2. Install dependencies:
   ```
   poetry install
   ```

3. Create a `.env` file in the project root:
   ```
   AZURE_OPENAI_ENDPOINT=your_azure_openai_endpoint
   AZURE_OPENAI_API_KEY=your_api_key  # Optional, if not using Azure AD auth
   ```

## Usage

Run the agent:

```
poetry run python -m agent
```

When you run the agent, you'll be prompted with an option:

```
Using deployment: ip-gpt-4o
Enter URL for a specific instruction set (or press Enter to use default): 
```

This allows you to:
1. Specify a URL for a custom instruction set
2. Enter a custom prompt to change the behavior of the agent
3. Press Enter to use the default settings

By providing a URL or custom prompt, you can modify how the agent behaves during the interaction.

