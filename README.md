# complwetion
[![pypi](https://img.shields.io/pypi/v/complwetion)](https://pypi.org/project/complwetion/)


Complwetion is a wrapper around an LLM provider and a Vector DB with common utilities like:
- crawling the web
- batching text into a list of desired sequence lengths
- Performing RAG
- vectorizing lists of sequences
- connecting to a vector db
- connecting to a LLM provider


The goal is to provide an elegant interface to build LLM powered backends. Here's how to use complwetion


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












