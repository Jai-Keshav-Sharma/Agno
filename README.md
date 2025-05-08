# Thai Cuisine Expert Agent and Multi-Agent Demos

This tutorial demonstrates several AI agent scripts using the [Agno](https://github.com/agnos-ai/agno) framework. The agents leverage LLMs (OpenAI or Groq), knowledge bases, and web tools to answer questions, retrieve information, and perform multi-agent collaboration. The tutorial is modular and can be extended for other domains.

## Features
- Use of LLMs (OpenAI GPT-4o or Groq Qwen) for natural language understanding
- Embedding and indexing of a PDF of Thai recipes for semantic search (in `agent_memory.py`)
- Web search fallback using DuckDuckGo
- Financial data retrieval using Yahoo Finance (in `multiple_agents.py`)
- Multi-agent collaboration (in `multiple_agents.py`)
- Simple agent demo (in `simpleagent.py`)

## Main Files
- `Basic Agents/agent_memory.py`: Main script for the Thai cuisine expert agent. Loads a PDF of Thai recipes into a vector database and answers questions using both the knowledge base and web search.
- `Basic Agents/multiple_agents.py`: Demonstrates a team of agents (web search and finance) collaborating to answer complex queries, such as comparing stock prices.
- `Basic Agents/simpleagent.py`: Minimal example of an agent using Groq LLM and DuckDuckGo web search.
- `Basic Agents/tmp/lancedb/`: Storage location for the LanceDB vector database used by `agent_memory.py`. No need to edit or commit these files.
- `requirements.txt`: Python dependencies for the tutorial.
- `.env.example`: Sample environment variable file (see below).
- `LICENSE`: MIT License for this tutorial.

## Setup Instructions
1. **Clone the repository**
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure environment variables**:
   - Copy `.env.example` to `.env` and fill in your API keys (see below).
4. **Run the scripts**:
   - Thai cuisine expert:
     ```bash
     python Basic\ Agents/agent_memory.py
     ```
   - Multi-agent demo:
     ```bash
     python Basic\ Agents/multiple_agents.py
     ```
   - Simple agent demo:
     ```bash
     python Basic\ Agents/simpleagent.py
     ```

## Environment Variables
Create a `.env` file in the tutorial root with the following content:

```
OPENAI_API_KEY=your_openai_api_key_here
GROQ_API_KEY=your_groq_api_key_here
```

- `OPENAI_API_KEY`: Required if using OpenAI models or embeddings.
- `GROQ_API_KEY`: Required if using Groq models.

**Never commit your `.env` file to version control.**

## Example Usage
- Thai cuisine expert: "How do I make chicken and galangal in coconut milk soup?"
- Multi-agent: "What is the stock price of Apple and compare it to the stock price of Google?"
- Simple agent: "Who is the President of the United States?"

## Documentation Links
- [Agno Documentation](https://github.com/agnos-ai/agno)
- [LanceDB Documentation](https://lancedb.github.io/lancedb/)
- [HuggingFace Transformers](https://huggingface.co/docs/transformers/index)
- [OpenAI API Docs](https://platform.openai.com/docs/)
- [Groq API Docs](https://console.groq.com/docs)

## License
See [LICENSE](LICENSE) for details. This tutorial is licensed under the MIT License.

## Security Note
- Do **not** share your `.env` file or any API keys publicly.
- Add `.env` to your `.gitignore` to prevent accidental commits.
