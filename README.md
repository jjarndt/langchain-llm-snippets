# Extracting Long-Term Memory from Conversations

This repository contains a Jupyter Notebook that demonstrates how to set up an agent capable of extracting long-term memories from a conversation, ideal for applications such as customized meal planning based on family preferences and restrictions. The setup utilizes Langchain to manage conversational logic and data handling efficiently.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- pip

### Installation

1. Install required Python libraries:
   ```bash
   pip install openai==1.12.0 langchain==0.1.6 langchain_openai==0.0.5 redis
   ```

2. Set up environment variables with your API keys and endpoints:
   ```bash
   export OPENAI_API_KEY="your-openai-api-key"
   export LANGCHAIN_TRACING_V2="true"
   export LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
   export LANGCHAIN_API_KEY="your-langchain-api-key"
   export LANGCHAIN_PROJECT="Meal-Planner"
   ```

## Usage

The main components are described here:

### Set up Agent: Memory Sentinel

- The Memory Sentinel evaluates a brief chat history to determine if a conversation contains details about a family's dining habits. It operates by analyzing messages and deciding whether they contain information worth recording.

### Set up Agent: Memory Manager

- The Memory Manager uses a Redis database to manage knowledge extracted from conversations. It supports creating, updating, and deleting knowledge entries based on the conversation analysis.

### Set up Agent: Meal Planner

- The Meal Planner creates meal plans based on the extracted memories. It uses the detailed dietary preferences and restrictions to suggest meals.

### Run the Agents

To execute the agents, you can use the provided Jupyter Notebook which includes all necessary code snippets and setup instructions.

### About Langchain

Langchain is a framework designed to enable developers to build applications that utilize large language models and complex workflows efficiently. For more information about Langchain and how it can be used in your projects, visit [Langchain's official website](https://www.langchain.com).
