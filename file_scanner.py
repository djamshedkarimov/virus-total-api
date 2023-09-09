import os

import requests

from config import base_url, api_version, API_KEY
from utils import get_file_type, check_file_size, get_file_from_directory, write_to_file


def scan_file(file, file_pw=None):
    """
    POST request to scan given file is malicious
    :param file: File name
    :param file_pw: File password (Optional)
    :return: response
    """
    _url, _is_small_enough = get_url_endpoint(file)
    headers = {
        "accept": "application/json",
        "x-apikey": API_KEY
    }
    files = {"file": (os.path.basename(file), open(file, "rb"), get_file_type(file))}

    payload = {}
    if not _is_small_enough:
        payload["url"] = generate_upload_url()
    if file_pw is not None:
        payload["password"] = file_pw
    print(f"PAYLOAD: {payload.keys()}")
    response = requests.post(_url, files=files, data=payload, headers=headers)
    json_resp = response.json()
    if response.status_code != 200:
        raise Exception(f"Get Upload Url failed code: {response.status_code} "
                        f"message: '{json_resp.get('error').get('message')}'")
    return json_resp


def get_url_endpoint(file):
    is_small_enough, _ = check_file_size(file)
    if is_small_enough:
        _url = f"{base_url}/{api_version}/files"
    else:
        _url = f"{base_url}/{api_version}/files/upload_url"
    return _url, is_small_enough


def generate_upload_url():
    """
    Function logic to generate a presigned URL for uploading large files
    @return Url to upload large files
    """
    _url = f"{base_url}/{api_version}/files/upload_url"
    headers = {
        "accept": "application/json",
        "x-apikey": API_KEY
    }
    response = requests.get(_url, headers=headers)
    json_resp = response.json()
    if response.status_code != 200:
        raise Exception(f"Get Upload Url failed code: {response.status_code} "
                        f"message: '{json_resp.get('error').get('message')}'")
    return json_resp['data']

