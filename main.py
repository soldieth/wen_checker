import json.decoder

import requests


def check(wallet):
    try:
        url = f"https://worker.jup.ag/jup-claim-proof/WENWENvqqNya429ubCdR81ZmD69brwQaaBYY6p3LCpk/{wallet}"
        r = requests.get(url).json()
        if 'amount' in r:
            print(f"{wallet}: {int(r['amount'])/100000}\n")
            return f"{wallet}: {int(r['amount'])/100000}\n"
    except json.decoder.JSONDecodeError:
        return ""


if __name__ == '__main__':
    with open('wallets.txt', 'r') as file:
        wallets = list(file.read().split("\n"))
    text = ""
    for wallet in wallets:
        text += check(wallet)

    with open("result.txt", "w") as file:
        file.write(text)
