# complwetion
[![pypi](https://img.shields.io/pypi/v/complwetion)](https://pypi.org/project/complwetion/)


Complwetion is a wrapper around an LLM provider and a Vector DB with common utilities like:
- crawling the web
- batching text into a list of desired sequence lengths
- Performing RAG
- vectorizing lists of sequences
- connecting to a vector db
- connecting to a LLM provider

The short term goal of complwetion is to provide an api to do auto-RAG. 1) Wire up a db, 2) Create an index, 3) encode and upsert some information, and 4) call a chat completion api with augmented context

Creating a library for building high performing auto-RAG chat completion backends is the near-longterm goal.


```python
pip install complwetion
```

## Using the Crawler Class

```python
import complwetion.crawler as crawler

url = "https://<full_url_here>"
domain = "<your_domain_here>"

headers = {
  // your headers
}

context = ssl._create_unverified_context()
crawler = crawler.Crawler(headers=headers, context=context, full_url=url, domain=domain)
crawler.crawl()
```

## Using the VectorDBService Class

```python
bot = vector_db_service.VectorDBService(environment="us-west1-gcp-free",
                                        device='cuda',
                                        model='all-MiniLM-L6-v2',
                                        index_name="<your_index_name>",
                                        batch_size=20,
                                        provider_API_key="<your_LLM_provider_api_key>",
                                        vectordb_API_key="<your_vertor_db_api_key>")

init = {"role": "system", "content": "< initilize the bot with persona, task, etc. >"}
response = bot.run_conversation("Do you guys do custom services? if so what are they and how much for each?", init=init)

print(res["choices"][0]["message"]["content"])
```

Currently, complwetion only supports pincone and openai. These have been hardcoded into the class. Which is shitty.












