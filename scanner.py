import argparse
import logging
import os

from analysis import get_scan_analysis, is_malicious
from file_scanner import scan_file
from url_scanner import scan_url
from utils import write_to_file, get_file_from_directory


def main():
    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser(description='Script for VirusTotal api automation.')

    parser.add_argument("--api-key", '-k', required=True, help="VirusTotal API key")
    parser.add_argument("--type", '-t', help="Type of scan url, file, etc...", required=True, choices=['url', 'file'])
    parser.add_argument("--url", '-u', help="URL to scan")
    parser.add_argument("--file", '-f', type=str, help="File to scan")
    parser.add_argument("--file-pwd", '-pwd', help="Optional file password")
    parser.add_argument("--output-file", action="store", default="output.json", help="File to store scan output")

    args = parser.parse_args()

    os.environ['api_key'] = str(args.api_key)
    __type = args.type
    __url = args.url
    __file = args.file
    __file_pw = args.file_pwd
    __output_file = args.output_file

    try:
        if __type.lower() == 'url':
            if __url is None:
                logging.error(f"Given URL: {__url}. Provide a valid URL to scan!")
                raise Exception(f"Given URL: {__url}. Provide a valid URL to scan!")

            scan_resp = scan_url(__url)
            report = get_scan_analysis(scan_resp['data']['id'])
            is_mal, msg = is_malicious(report, __type)

            if is_mal:
                write_to_file(__output_file, report)

            logging.info(f'URL: Found {msg}!')

        elif __type.lower() == 'file':
            if __file is None:
                logging.error(f"Given file: {__file}. Provide a valid file to scan!")
                raise Exception(f"Given file: {__file}. Provide a valid file to scan!")

            scan_resp = scan_file(get_file_from_directory(__file), __file_pw)
            report = get_scan_analysis(scan_resp['data']['id'])
            is_mal, msg = is_malicious(report, __type)

            if is_mal:
                write_to_file(__output_file, report)

            logging.info(f'File is {msg}!')

        else:
            logging.error(f"Unknown type: {__type}. Only 'url' and 'file' are supported.")
            raise Exception(f"Unknown type: {__type}. Only 'url' and 'file' are supported.")

    except Exception as e:
        logging.error(f"An error occurred: {e}")


if __name__ == '__main__':
    print("--------------------------- START ---------------------------")
    try:
        main()
    finally:
        print("--------------------------- END ---------------------------")