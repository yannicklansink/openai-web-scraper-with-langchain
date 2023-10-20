from bs4 import BeautifulSoup
from playwright.async_api import async_playwright
from langchain.chat_models import ChatOpenAI
from langchain.chains import create_extraction_chain, create_extraction_chain_pydantic
from dotenv import load_dotenv
import os
import asyncio

from pydantic import BaseModel, Field
from web_scraper import run_playwright

from flask import Flask, render_template_string

app = Flask(__name__)


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
    return [item.dict() for item in result]


# Execute async function main
def run_main():
    return asyncio.run(main())


# web api frontend
@app.route('/')
def index():
    response_dict = run_main()
    print(response_dict)
    return render_template_string(template, response_dict=response_dict)

template = """
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
  </head>
  <body>
    <div class="container">
      <h1 class="mt-5">Web Scraping Results</h1>
      <table class="table mt-3">
        <thead>
          <tr>
            <th>Name</th>
            <th>Points</th>
            <th>Comments</th>
            <th>URL</th>
          </tr>
        </thead>
        <tbody>
          {% for item in response_dict %}
          <tr>
            <td>{{ item.name }}</td>
            <td>{{ item.points }}</td>
            <td>{{ item.comments }}</td>
            <td>{{ item.url }}</td>
          </tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
  </body>
</html>
"""

if __name__ == '__main__':
    app.run(debug=True)

