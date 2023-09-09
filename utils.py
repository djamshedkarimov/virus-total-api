import base64
import json
import mimetypes
import os


def generate_url_identifier(url):
    return base64.urlsafe_b64encode(url.encode()).decode().strip("=")


def get_file_type(file):
    mime_type, _ = mimetypes.guess_type(file)
    if not mime_type:
        raise Exception(f"File type for '{file}' is not recognized.")
    return mime_type


def check_file_size(file, max_size_mb=32):
    """
    Function to check given file size is not greater than max size
    @param file: file name
    @param max_size_mb: default max file size in MB
    @return: tuple boolean & file siz in MB
    """
    try:
        file_size = os.path.getsize(file)
        max_size_bytes = max_size_mb * 1024 * 1024  # Convert MB to bytes

        if file_size > max_size_bytes:
            return False, file_size
        else:
            return True, file_size
    except FileNotFoundError:
        return False, 0


def get_file_from_directory(file_name):
    file_path = os.path.join('files', file_name)
    if os.path.exists(file_path):
        return file_path
    else:
        print(f"File '{file_name}' not found in the directory.")
        return None


def write_to_file(file_name, data):
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)
