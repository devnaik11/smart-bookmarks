import trafilatura

def extract_web_content(url: str) -> dict:
    """Download a web page and return its title and main tect."""
    downloaded = trafilatura.fetch_url(url)
    if downloaded is None:
        raise ValueError("Could not download the web page.")

    text = trafilatura.extract(downloaded)
    if not text:
        raise ValueError("Could not find readable text on the page.")

    metadata = trafilatura.extract_metadata(downloaded)
    title = metadata.title if metadata and metadata.title else url

    return {"url": url, "title": title, "text": text}