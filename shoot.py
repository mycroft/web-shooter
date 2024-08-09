#!/usr/bin/env python

import argparse

from base64 import b64decode

from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.print_page_options import PrintOptions

from slugify import slugify

parser = argparse.ArgumentParser(description='shoot urls to pdf/png')
parser.add_argument('--engine', type=str, help='engine to use (chrome or firefox)')
parser.add_argument('--add-numbers', dest='numbers', type=bool, action=argparse.BooleanOptionalAction,
                    help='automatically add a number as a prefix')
parser.add_argument('--enable-png', dest='png', type=bool, action=argparse.BooleanOptionalAction,
                    help='generate PNGs screenshots', default=False)
parser.add_argument('--enable-pdf', dest='pdf', type=bool, action=argparse.BooleanOptionalAction,
                    help='generate PDFs files', default=True)
parser.add_argument('urls', type=str, nargs='+', help='urls to scrape')

args = parser.parse_args()

if args.png is not True and args.pdf is not True:
    parser.error('either --enable-png or --enable-pdf is required')

if args.engine == 'chrome':
    options = ChromeOptions()
    options.add_argument('--headless')
    # options.add_argument('--disable-gpu')

    driver = webdriver.Chrome(options)
else:
    options = FirefoxOptions()
    options.add_argument('--headless')

    driver = webdriver.Firefox(options)


idx = 1

for url in args.urls:
    slugified_url = slugify(url)
    prefix = ''

    if args.numbers:
        prefix = '{:03}-'.format(idx)
        idx += 1

    pdf_file_name = "{}{}.pdf".format(prefix, slugified_url)
    png_file_name = "{}{}.png".format(prefix, slugified_url)

    print("getting page {}...".format(url))
    driver.get(url)

    if args.png:
        print("doing screenshot, into {}...".format(png_file_name))
        driver.get_screenshot_as_file(png_file_name)

    if args.pdf:
        print_options = PrintOptions()
        print_options.page_width = 21.0
        print_options.page_height = 29.7
        print_options.background = True

        print("printing page...")
        res = driver.print_page(print_options)

        with open(pdf_file_name, 'wb') as fd:
            fd.write(b64decode(res.encode('ascii')))

        print("wrote {}".format(pdf_file_name))

    if len(args.urls) > 1:
        print()

driver.close()
