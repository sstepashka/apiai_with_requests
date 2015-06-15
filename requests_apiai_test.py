#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json

def main():
    CLIENT_ACCESS_TOKEN = '09604c7f91ce4cd8a4ede55eb5340b9d'
    SUBSCRIBTION_KEY = '4c91a8e5-275f-4bf0-8f94-befa78ef92cd'

    url = 'https://api.api.ai/v1/query'

    payload = {
        'lang': 'en',
        'sessionId': '<session id>',
        # 'contexts': [],
        # 'resetContexts': False,
        # 'timezone': None,
    }

    files = {
        'request': ('request.json', json.dumps(payload), 'application/json'),
        'voiceData': ('voiceData.raw', open('ann_smith.wav', 'rb'), 'audio/wav')
    }

    headers = {
        'Accept': 'application/json',
        # 'Accept-Encoding': 'gzip, deflate',
        'Authorization': ('Bearer %s' % CLIENT_ACCESS_TOKEN),
        'ocp-apim-subscription-key': SUBSCRIBTION_KEY,
    }

    response = requests.post(url, files=files, headers=headers)

    print response.text

if __name__ == '__main__':
    main()