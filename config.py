import logging
import os

base_url = 'https://www.virustotal.com/api'
api_version = 'v3'

# Pass your API Key here or provide in command line as -k=<YOUR API KEY HERE>
API_KEY='ADD YOUR API KEY HERE'
_cached_api_key = None


def get_api_key():
    global _cached_api_key
    # If API key is already cached, return it
    if _cached_api_key is not None:
        return _cached_api_key
    logging.info('Get API Key')
    api_key = os.getenv('api_key')

    if api_key is not None:
        api_key = API_KEY

    logging.info(f'API_KEY: {api_key}')
    # Cache the API key before returning
    _cached_api_key = api_key
    return api_key