# Certbot deploy hook for AdGuardHome
## How to intall:
* Install Python in your system
* Go to path of this script
* Run `python -m venv venv` to install venv
## Crontab usage example
```sh
0 0 * * 0 certbot renew --deploy-hook "cd /path-to-script && ./venv/bin/python ."
```