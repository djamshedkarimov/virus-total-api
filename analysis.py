import requests

from config import base_url, api_version, API_KEY


def get_scan_analysis(scan_id):
    """
    @summary: Get URL/File scan analysis
    :param scan_id: id from scan_urls() or scan_files() response
    :return: analysis response
    """
    _url = f"{base_url}/{api_version}/analyses/{scan_id}"
    headers = {
        "accept": "application/json",
        "X-Apikey": API_KEY,
    }
    response = requests.get(_url, headers=headers)
    json_resp = response.json()
    if response.status_code != 200:
        raise Exception(f"Scan analysis failed code: {response.status_code} "
                        f"message: '{json_resp.get('error').get('message')}'")
    return json_resp


def is_malicious(data, _type):
    """
    Check if given json data is malicious
    @data: data to be analyzed
    @_type: Type of scan url/file
    @return: Boolean & message
    """
    stats = data['data']['attributes']['stats']
    malicious = stats['malicious']
    suspicious = stats.get('suspicious', 0)

    if _type.lower() == 'url':
        _is_mal = malicious > 0 or suspicious > 0
        _message = f"{malicious} malicious and {suspicious} suspicious" if _is_mal else "not malicious or suspicious"
    elif _type.lower() == 'file':
        _is_mal = malicious > 0
        _message = "malicious" if _is_mal else "not malicious"
    else:
        raise Exception(f"Invalid type {_type} given")
    return _is_mal, f"Found {_message}!"

