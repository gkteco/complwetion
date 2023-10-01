import requests
import re
import urllib.request
from bs4 import BeautifulSoup
from collections import deque
from html.parser import HTMLParser
from urllib.parse import urlparse
import os
import urllib.request
from tqdm import tqdm

HTTP_URL_PATTERN = r'^http[s]*://.+'
class HyperlinkParser(HTMLParser):
  def __init__(self):
    self.hyperlinks = []
    HTMLParser.__init__(self)

  def handle_starttag(self, tag, attrs):
    attrs = dict(attrs)

    if tag == "a" and "href" in attrs:
      self.hyperlinks.append(attrs["href"])


class Crawler:


    def __init__(self, headers, context, full_url, domain):
        self.headers = headers
        self.context = context
        self.full_url = full_url
        self.domain = domain
        self.res = urllib.request.Request(full_url, headers=headers)

    def get_hyperlinks(self, full_url: str):
        try:
            with urllib.request.urlopen(self.res, context=self.context) as response:
                if not response.info().get('Content-Type').startswith("text/html"):
                    return []
                html = response.read().decode('utf-8')
        except Exception as e:
            print(e)
            return []

        parser = HyperlinkParser()
        parser.feed(html)
        return parser.hyperlinks


    def get_domain_hyperlinks(self):
        clean_links = []
        for link in set(self.get_hyperlinks(self.full_url)):
            clean_link = None

            # If the link is a URL, check if it is within the same domain
            if re.search(HTTP_URL_PATTERN, link):
                # Parse the URL and check if the domain is the same
                url_obj = urlparse(link)
                if url_obj.netloc == self.domain:
                    clean_link = link

            # If the link is not a URL, check if it is a relative link
            else:
                if link.startswith("/"):
                    link = link[1:]
                elif link.startswith("#") or link.startswith("mailto:"):
                    continue
                clean_link = "https://" + self.domain + "/" + link

            if clean_link is not None:
                if clean_link.endswith("/"):
                    clean_link = clean_link[:-1]
                clean_links.append(clean_link)

        # Return the list of hyperlinks that are within the same domain
        return list(set(clean_links))




    def crawl(self):
        # Parse the URL and get the domain
        local_domain = urlparse(self.full_url).netloc

        # Create a queue to store the URLs to crawl
        queue = deque([self.full_url])

        # Create a set to store the URLs that have already been seen (no duplicates)
        seen = set([self.full_url])

        # Create a directory to store the text files
        if not os.path.exists("text/"):
                os.mkdir("text/")

        if not os.path.exists("text/"+local_domain+"/"):
                os.mkdir("text/" + local_domain + "/")
        # While the queue is not empty, continue crawling
        while queue:

            # Get the next URL from the queue
            url = queue.pop()
            print(url) # for debugging and to see the progress

            # Save text from the url to a <url>.txt file
            with open('text/'+local_domain+'/'+url[8:].replace("/", "_") + ".txt", "w", encoding="utf-8") as f:

                # Get the text from the URL using BeautifulSoup
                soup = BeautifulSoup(requests.get(url, headers=self.headers, verify=False).text, "html.parser")

                # Get the text but remove the tags
                text = soup.get_text()

                # If the crawler gets to a page that requires JavaScript, it will stop the crawl
                if ("You need to enable JavaScript to run this app." in text):
                    print("Unable to parse page " + url + " due to JavaScript being required")

                # Otherwise, write the text to the file in the text directory
                f.write(text)

            # Get the hyperlinks from the URL and add them to the queue
            for link in self.get_domain_hyperlinks():
                if link not in seen:
                    queue.append(link)
                    seen.add(link)

    def remove_newlines(self, serie):
        serie = serie.replace('\n', ' ')
        serie = serie.replace('\\n', ' ')
        serie = serie.replace('  ', ' ')
        serie = serie.replace('  ', ' ')
        return serie


    def process_data(self):
        data = []
        print("Processing files in /text/" + self.domain)
        for file in tqdm(os.listdir("text/" + self.domain)):

            with open("text/" + self.domain + "/" + file, "r", encoding="utf") as f:
                raw_text = f.read()
                data.append(raw_text)
        return [self.remove_newlines(x) for x in data]

