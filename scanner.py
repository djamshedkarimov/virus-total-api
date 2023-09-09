import argparse

from analysis import get_scan_analysis, is_malicious
from file_scanner import scan_file
from url_scanner import scan_url
from utils import write_to_file, get_file_from_directory


def main():
    parser = argparse.ArgumentParser(description='Script for web reconnaissance and enumeration.')

    parser.add_argument("--type", '-t', help="Type of scan url, file, etc...")
    parser.add_argument("--url", '-u', help="URL to scan")
    parser.add_argument("--file", '-f', type=str, help="File to scan")
    parser.add_argument("--file-pwd",  '-pwd', help="Optional file password")
    parser.add_argument("--output-file", action="store", default="output.json", help="File to store scan output")

    args = parser.parse_args()

    __type = args.type
    __url = args.url
    __file = args.file
    __file_pw = args.file_pwd
    __output_file = args.output_file

    if __type.lower() == 'url':
        if __url is not None:
            scan_resp = scan_url(__url)
            report = get_scan_analysis(scan_resp['data']['id'])
            is_mal, msg = is_malicious(report, __type)
            if is_mal:
                write_to_file(__output_file, report)
            print(msg)
        else:
            print(f"Given url: {__url}. Provide valid url to scan!")
            raise Exception(f"Given url: {__url}. Provide valid url to scan!")
    elif __type.lower() == 'file':
        if __file is not None:
            scan_resp = scan_file(get_file_from_directory(__file), __file_pw)
            report = get_scan_analysis(scan_resp['data']['id'])
            is_mal, msg = is_malicious(report, __type)
            if is_mal:
                write_to_file(__output_file, report)
            print(msg)
        else:
            print(f"Given url: {__file}. Provide valid url to scan!")
            raise Exception(f"Given url: {__file}. Provide valid url to scan!")


if __name__ == '__main__':
    print("--------------------------- START ---------------------------")
    try:
        main()
    finally:
        print("--------------------------- END ---------------------------")