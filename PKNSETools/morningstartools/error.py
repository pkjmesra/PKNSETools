"""
    The MIT License (MIT)

    Copyright (c) 2023 pkjmesra

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

"""


def not_200_response(url,response):
    """
    This function raise a ConnectionError if the status code a requests is not 200.

    """
    if response is None:
        raise ConnectionError(f"Error for the api {url}.")
    if not response.status_code == 200:
        raise ConnectionError(f"Error {response.status_code} for the api {url}. Message : {response.reason}.")


def no_site_error(code, name, country, site):
    """ 
    This function raise a ValueError if the selected country is "us" or a site is not selected.
    
    """
    
        
    if not site or country == 'us':
        if country:
            raise ValueError(f"The funds of the country {country} cannot be scraped.")
        else:
            raise ValueError(f"The funds {name} ({code}) cannot be scraped.")



    