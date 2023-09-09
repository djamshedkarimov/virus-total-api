# VirusTotal API Reference Automation

This project demonstrates how to automate interactions with the VirusTotal API using Python to perform various tasks such as scanning files and URLs, retrieving scan reports, and accessing different API endpoints.

## Table of Contents

- [Project Overview](#project-overview)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [API Key](#api-key)
  - [Running the Scripts](#running-the-scripts)
- [API Reference](#api-reference)

## Project Overview

This project provides Python scripts and examples that demonstrate how to interact with various VirusTotal API endpoints using the official API documentation. It covers topics such as authentication, making requests, handling responses, and utilizing different API features.

## Getting Started

### Prerequisites

- Python 2.x or 3.x installed
- VirusTotal API key (sign up at https://www.virustotal.com/)
- Internet connection

### Installation

1. Clone this repository:
   ```sh
   git clone https://github.com/djamshedkarimov/virus-total.git
2. Install virtual environment:
    ```sh
    pip install venv
3. Activate virtual environment Linux/MacOS:
   ```sh
   source venv/bin/activate
4. Activate virtual environment Windows:   
    ```sh
    venv\Scripts\activate
5. Install required packages
    ```sh
   pip install -r requirements.txt
   
### Usage

#### API Key
Replace "YOUR_API_KEY" in the scripts with your actual VirusTotal API key.

#### Running the Scripts
Navigate to the project directory and execute the Python scripts.
Example usage:
- Scan url:
  - python main.py -t=url -u="your-website.com"
- Scan file:
  - python main.py -t=file -u="your-file.png" -pwd="Optional file password"

### API Reference
Refer to the [VirusTotal API Documentation](https://developers.virustotal.com/reference/overview) for detailed information about available endpoints, request parameters, response formats, and more.
