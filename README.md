# web-shooter

## Usage

```sh
$ python --version
Python 3.12.4

$ python -m venv .env
$ source .env/bin/activate.fish
(.env) $ pip install -r requirements.txt
...

(.env) $ python shoot.py --help
usage: shoot.py [-h] [--engine ENGINE] [--add-numbers | --no-add-numbers] [--enable-png | --no-enable-png] [--enable-pdf | --no-enable-pdf]
                urls [urls ...]

shoot urls to pdf/png

positional arguments:
  urls                  urls to scrape

options:
  -h, --help            show this help message and exit
  --engine ENGINE       engine to use (chrome or firefox)
  --add-numbers, --no-add-numbers
                        automatically add a number as a prefix
  --enable-png, --no-enable-png
                        generate PNGs screenshots
  --enable-pdf, --no-enable-pdf
                        generate PDFs files

(.env) $ python shoot.py --engine firefox --add-numbers https://awasu.com/weblog/2022/01/ https://awasu.com/weblog/git-guts/store/
getting page https://awasu.com/weblog/2022/01/...
doing screenshot, into 001-https-awasu-com-weblog-2022-01.png...
printing page...
wrote 001-https-awasu-com-weblog-2022-01.pdf

getting page https://awasu.com/weblog/git-guts/store/...
doing screenshot, into 002-https-awasu-com-weblog-git-guts-store.png...
printing page...
wrote 002-https-awasu-com-weblog-git-guts-store.pdf

(.env) $
```
