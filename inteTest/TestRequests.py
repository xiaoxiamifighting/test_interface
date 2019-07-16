
import pytest
import requests
import logging
import json
class TestRequests(object):
    def test_get(self):
        r = requests.get("https://testerhome.com/api/v3/topics.json?limit=2")
        logging.info(r.headers)
        print(json.dumps(r.json(),indent=2))
