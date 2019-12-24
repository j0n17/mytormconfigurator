import json
import requests
import argparse
from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import TerminalFormatter

ALLOWED_COMMANDS = [
    'show',
    'set'
]

ALLOWED_ACTTIONS = [
    'single',
    'double',
    'long',
    'generic'
]

URL_INFO = "api/v1/device"
URL_ACTION = "api/v1/action"


def get(url: str):
    res = requests.get(url)
    if res.status_code == 200:
        print(highlight(json.dumps(res.json(), indent=4, sort_keys=True),
                        JsonLexer(), TerminalFormatter()))
    else:
        print("Error : (%s) %s - %s" %
              (res.status_code, res.reason, res.text))
        exit(1)


def post(url: str, data: str):
    res = requests.post(url, data=data)
    if res.status_code == 200:
        print("ok")
    else:
        print("Error : (%s) %s - %s" %
              (res.status_code, res.reason, res.text))
        exit(1)


def clean_host(host: str) -> str:
    return "http://%s" % host.replace('http://', '').replace('https://', '')


def show(host: str):
    get("%s/%s" % (clean_host(host), URL_INFO))


def set_action(host: str, action: str, value: str):
    if action not in ALLOWED_ACTTIONS:
        print("Allowed actions are : %s" % ALLOWED_ACTTIONS)
        exit(1)
    post("%s/%s/%s" % (clean_host(host), URL_ACTION, action), value)


def main():
    p = argparse.ArgumentParser()
    s = p.add_subparsers(dest='subcommand', required=True)

    p_show = s.add_parser('show')
    p_show.add_argument(
        'host', help='Button(+)\'s hostname or IP address')

    p_set = s.add_parser('set')
    p_set.add_argument(
        'host', help='Button(+)\'s hostname or IP address')
    p_set.add_argument(
        'action', help='Action to update')
    p_set.add_argument(
        'value', help='New value')

    args = p.parse_args()
    command = args.subcommand

    if command == 'set':
        set_action(args.host, args.action, args.value)
    else:
        show(args.host)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
    # except Exception as e:
    #    print(e)
