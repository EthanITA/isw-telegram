import json
import os

import simple_salesforce
from simple_salesforce import Salesforce, format_soql

secrets = os.environ if os.environ.get('is_production') else json.load(open(os.path.join("secrets")))

username = secrets["sf_username"]
password = secrets["sf_password"]
security_token = secrets["sf_security_token"]
sf = Salesforce(username=username, password=password, security_token=security_token)


def query_all(query: str, *args, **kwargs):
    global sf
    try:
        return sf.query_all(format_soql(query, *args, **kwargs))
    except simple_salesforce.exceptions.SalesforceExpiredSession as sessions_expired:
        print(sessions_expired)
        sf = Salesforce(username=username, password=password, security_token=security_token)
        return sf.query_all(format_soql(query, *args, **kwargs))
