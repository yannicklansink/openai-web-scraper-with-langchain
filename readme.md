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

### How did the data change?

Our web scraper scraped the following data:

#####

[{'name': 'In search of the least viewed article on Wikipedia', 'points': '90', 'comments': 44, 'url': 'colinmorris.github.io'}, {'name': 'Nakatomi Space', 'points': '86', 'comments': 40, 'url': 'bldgblog.com'}, {'name': 'Find the date of your birthday in the number pi', 'points': '97', 'comments': 63, 'url': 'mypiday.com'}, {'name': 'Versioning data in Postgres? Testing a Git like approach', 'points': '34', 'comments': 13, 'url': 'specfy.io'}, {'name': 'Nonprofit hospitals skimp on charity while CEOs reap millions, report finds', 'points': '77', 'comments': 23, 'url': 'arstechnica.com'}, {'name': 'Hexagonal Grids (2013)', 'points': '80', 'comments': 8, 'url': 'redblobgames.com'}, {'name': 'Using extra Firefox profiles to make my life better', 'points': '296', 'comments': 192, 'url': 'utoronto.ca'}, {'name': "AI tidies up Wikipedia's references – and boosts reliability", 'points': '24', 'comments': 5, 'url': 'nature.com'}, {'name': 'Humming-Birds', 'points': '12', 'comments': 1, 'url': 'c82.net'}, {'name': 'Cops Are Suing a Teen for Invasion of Privacy After False Arrest Vid Goes Viral', 'points': '41', 'comments': 10, 'url': 'vice.com'}, {'name': 'Encrypted traffic interception on Hetzner and Linode targeting Jabber service', 'points': '56', 'comments': 10, 'url': 'org.ru'}, {'name': 'UpCodes (YC S17) is hiring remote engineers to help architects with compliance', 'points': 'N/A', 'comments': 0, 'url': 'up.codes'}, {'name': 'Solreader: E-Ink Smart Glasses for Reading', 'points': '34', 'comments': 37, 'url': 'solreader.com'}, {'name': 'The Unix Game', 'points': '112', 'comments': 25, 'url': 'unixgame.io'}, {'name': "It's easy to screw up on breaking news. But you have to admit when you do", 'points': '120', 'comments': 93, 'url': 'natesilver.net'}, {'name': 'Nota is a language for writing documents, like academic papers and blog posts', 'points': '434', 'comments': 145, 'url': 'nota-lang.org'}, {'name': 'Eclipse October 2023', 'points': '3', 'comments': 0, 'url': 'gridstatus.io'}, {'name': 'GnuCash Tutorial and Concepts Guide', 'points': '108', 'comments': 88, 'url': 'gnucash.org'}, {'name': 'Everything Looks Like a Nail', 'points': '8', 'comments': 0, 'url': 'wheresyoured.at'}, {'name': 'Some advice I would give to a junior DevOps Engineer', 'points': '15', 'comments': 32, 'url': 'oschvr.com'}, {'name': 'We caught technicians snooping on our personal devices', 'points': '55', 'comments': 27, 'url': 'cbc.ca'}, {'name': 'Show HN: Practice all the songs you know on your musical instrument', 'points': '11', 'comments': 2, 'url': 'github.com/lorendb'}, {'name': 'Confidential computing and AI fit together', 'points': '6', 'comments': 0, 'url': 'edgeless.systems'}, {'name': 'Friday Factorio Facts #381 – Space Platforms', 'points': '103', 'comments': 14, 'url': 'factorio.com'}, {'name': 'The Tech Industry Has a New Plan to Stop Proliferation of Right to Repair Laws', 'points': '15', 'comments': 0, 'url': '404media.co'}, {'name': 'OS/2 Warp, PowerPC Edition', 'points': '87', 'comments': 38, 'url': 'kev009.com'}, {'name': "Jon Stewart's Show on Apple Is Ending", 'points': '103', 'comments': 90, 'url': 'nytimes.com'}, {'name': 'A tutorial for the sam command language (1986) [pdf]', 'points': '31', 'comments': 8, 'url': 'cat-v.org'}, {'name': 'Which Interpreters Are Faster, AST or Bytecode?', 'points': '71', 'comments': 11, 'url': 'stefan-marr.de'}, {'name': 'Webb detects quartz crystals in clouds of hot gas giant', 'points': '71', 'comments': 21, 'url': 'phys.org'}]

Then we used our Pydantic schema to validate and structure the data based on that. You can look at it as some sort of blueprint.

Utilize Langchain to create a data extraction chain. This chain will use the Pydantic schema to validate and structure the scraped data.

Then we displayed the data on our Flask web application for easy visualition, but you can do whatever you want with it at this point.

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
