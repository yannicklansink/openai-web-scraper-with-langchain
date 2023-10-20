### Why use function calling:

Function calling is a useful way to get structured output from an LLM for a wide range of purposes. By providing schemas for "functions", the LLM will choose one and attempt to output a response matching that schema.

Though the name implies that the LLM is actually running code and calling a function, that is not completly true, it is more accurate to say that the LLM is populating parameters that match the schema for the arguments a hypothetical function would take.

### Why use function calling with web scraping:

Large Language Models (LLMs), are optimised to receive unstructured data in the form of conversational natural language.
Like a peach of text that you can scrape froma a website.

This unstructured data is then structured, processed and subsequently unstructured again in the form of natural language output.

LangChain function calling in the context of web scraping facilitates a structured, efficient, and integrated approach towards data gathering, processing, and application development, especially in scenarios involving large language models

### Why use a pydantic class over a JSON object

Using a Pydantic class over a JSON object can offer several advantages when working with data in Python, especially in terms of validation and type checking,

Pydantic classes provide a way to define a schema for data, ensuring that the data adheres to specified types and constraints. This can be especially beneficial in applications that handle data from various sources, where ensuring consistency and correctness of data is crucial. In contrast, JSON objects don't have a built-in mechanism for validation or type enforcement, which could lead to potential issues when processing the data.

Pydantic also enables the use of editor support, autocomplete, and other development functionality that might be handy for you to use.

https://twitter.com/ethanjdev/status/1676320043456397312

### Thougths on using this approach for web scraping

### What can you do further

- Efficient data harvesting
  By marrying OpenAI function calling with LangChain's scraping mechanisms, you could create robust pipelines for efficiently harvesting data from the web.

Some more examples include:

- Automated Market Analysis Platform:
  Create a platform that automatically scrapes financial news, market data, and analyst reports to provide real-time market analysis and insights. Utilize OpenAI to process and analyze the collected data to generate actionable investment recommendations.

- Competitor Monitoring System:
  Develop a system that continuously monitors competitors’ websites, press releases, and social media channels to track their product releases, pricing changes, and marketing campaigns. Use OpenAI to summarize findings and compare strategies over time.

- Automated Supply Chain Monitoring:
  Build a system that continuously monitors global supply chain information by scraping data from logistics providers, governmental trade databases, and news outlets.
