from scrapers.universal_google import scrape_google_results

def get_prices(query, country, groq_api_key):
    return scrape_google_results(query, country, groq_api_key)