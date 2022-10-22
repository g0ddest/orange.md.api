import requests


class Orange:

    wassup = None
    lang = "EN"
    APP_VERSION = "6.3.0"
    OS_VERSION = "6.0"
    PLATFORM = "android"
    COUNTRY = "MD"
    AUTH_HOST = "https://sso.orange.md"
    HOST = "https://sso.orange.com"

    def __init__(self, username, password, lang="EN"):
        self.lang = lang
        self.wassup = self.login(username, password)

    def login(self, username, password):
        r = requests.post(self.AUTH_HOST + "/be/index.php",
        params={"a": "login"},
        json={
            "username": username,
            "password": password,
            "client": "webcare"
        })
        if r.status_code > 299:
            raise Exception
        wassup = r.json()['cooses'].split(";")[0].split("=")[1]
        return {"wassup": wassup}

    def balance(self):
        r = requests.get(
            self.HOST + "/eden/v2/get",
            params={
                "language": self.lang,
                "subsection": ["account", "balance"],
                "appVersion": self.APP_VERSION,
                "osVersion": self.OS_VERSION,
                "platform": self.PLATFORM,
                "country": self.COUNTRY
            },
            cookies=self.wassup)
        return r.json()

    def services_list(self):
        r = requests.get(
             self.HOST + "/eden/v2/options",
             params={
                 "language": self.lang,
                 "appVersion": self.APP_VERSION,
                 "osVersion": self.OS_VERSION,
                 "platform": self.PLATFORM,
                 "country": self.COUNTRY
             },
             cookies=self.wassup)
        return r.json()

    def subscribe_daily_bonus(self):
        return self.subscribe("SPO_DAILY_BONUS_25MB")

    def subscribe(self, service):
        r = requests.post(
            self.HOST + "/eden/v2/manageContractOptions",
            params={
                "language": self.lang,
                "appVersion": self.APP_VERSION,
                "osVersion": self.OS_VERSION,
                "platform": self.PLATFORM,
                "country": self.COUNTRY,
                "operation": "Subscribe",
                "id": service
            },
            cookies=self.wassup)
        return r.text