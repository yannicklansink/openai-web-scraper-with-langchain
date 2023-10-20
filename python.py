from bs4 import BeautifulSoup
from playwright.async_api import async_playwright
from langchain.chains import create_extraction_chain
from langchain.chat_models import ChatOpenAI
from langchain.chains import create_extraction_chain
from dotenv import load_dotenv
import os
import asyncio

from pydantic import BaseModel, Field
from web_scraper import run_playwright

load_dotenv()
openai_key = os.getenv("openai_key")

schema = {
        "properties": {
            "name": {"type": "string"},
            "points": {"type": "integer"},
            "comments": {"type": "integer"},
            "url": {"type":"string"}
        },
        "required": ["name", "points", "comments"],
    }

async def main():
    site_data = await run_playwright("https://news.ycombinator.com/news")
    print(site_data)

    

    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613", openai_api_key=openai_key)
    
    extraction_chain = create_extraction_chain(schema, llm)
    result = extraction_chain.run(site_data)
    print(result)


# Execute async function main
asyncio.run(main())

