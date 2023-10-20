from bs4 import BeautifulSoup
from playwright.async_api import async_playwright
from langchain.chat_models import ChatOpenAI
from langchain.chains import create_extraction_chain, create_extraction_chain_pydantic
from dotenv import load_dotenv
import os
import asyncio

from pydantic import BaseModel, Field
from web_scraper import run_playwright

load_dotenv()
openai_key = os.getenv("openai_key")

# Step 2: Implementing a pydantic class. Explain why!
class RecordWebsite(BaseModel):
     name: str = Field(..., description="The name of the post", example="What's new in Python")
     points: str = Field(..., description="The points of the post")
     comments: int = Field(..., description="The number of comments of the post")
     url: str = Field(..., description="The url of the post")


async def main():
    site_data = await run_playwright("https://news.ycombinator.com/news")
    print(site_data)

    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613", openai_api_key=openai_key)
    
    result = create_extraction_chain_pydantic(pydantic_schema=RecordWebsite, llm=llm).run(site_data)

    # list comprehension
    response_dict = [item.dict() for item in result]
    print(response_dict)


# Execute async function main
asyncio.run(main())

