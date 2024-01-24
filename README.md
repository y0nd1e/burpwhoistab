# WHOIS Lookup Burp Extension

## Overview

The **WHOIS Lookup Burp Extension** is a Burp Suite extension that allows you to perform WHOIS lookups on domains directly from Burp Suite using whosifreak API. It provides a convenient way to gather information about a domain quickly during your web security assessments. 

## Features

- **Domain WHOIS Lookup**: Easily retrieve WHOIS information for a given domain.
- **Integration with Burp Suite**: Seamlessly integrated with Burp Suite for a streamlined workflow.
- **Context Menu Integration**: You can right-click on a request in Burp Suite and send the selected domain to the WHOIS lookup tool.
- **Clean and User-Friendly Interface**: The extension features a clean and intuitive user interface for a hassle-free experience.

## Installation

1. Clone this repository or download the `whois_lookup.py` file.
2. Open Burp Suite and navigate to the "Extender" tab.
3. Click on the "Add" button in the "Extensions" tab.
4. Select "Jython" as the extension type and specify the path to the `whois_lookup.py` file.
5. Click "Next" and confirm the installation.

## Usage

1. Open Burp Suite.
2. Navigate to the "Extender" tab.
3. Click on the "WHOIS Lookup" tab to access the tool.

### Manual Domain Lookup

1. Enter the domain name in the "Domain" field.
2. Click the "Lookup" button.
3. The WHOIS information will be displayed in the response area below.

### Context Menu Integration

1. In Burp Suite, right-click on a request containing a domain name.
2. Select "Send to WHOIS Lookup" from the context menu.
3. The domain will be automatically populated in the "Domain" field, and you can click the "Lookup" button to retrieve WHOIS information.

## Examples
![example](https://github.com/y0nd1e/burpwhoistab/assets/157593415/93fa125d-11ce-4379-91f8-9f0a05e33805)


## Configuration

You need to set your API key in the code. Locate the `API_KEY` variable within the `BurpExtender` class and replace `"APIKEY"` with your actual API key.

```python
# Hardcode the API key here
API_KEY = "YOUR_API_KEY"


