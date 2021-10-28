import datetime

BASE_HOSTNAME = "www.smartmetertexas.com"
BASE_URL = "https://" + BASE_HOSTNAME
BASE_ENDPOINT = BASE_URL + "/api"
AUTH_ENDPOINT = "/user/authenticate"
DASHBOARD_ENDPOINT = "/dashboard"
LATEST_OD_READ_ENDPOINT = "/usage/latestodrread"
METER_ENDPOINT = "/meter"
OD_READ_ENDPOINT = "/ondemandread"

USER_AGENT_TEMPLATE = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/95.0.{BUILD}.{REV} "
    "Safari/537.36 "
    "Edg/95.0.{BUILD}.{REV}"
)
CLIENT_HEADERS = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Content-Type": "application/json;charset=UTF-8",
    "Cache-Control": "no-cache",
    "Pragma": "no-cache",
    "DNT": "1",
    "Connection": "keep-alive",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Origin": BASE_URL
}

API_ERROR_KEY = "errormessage"
TOKEN_EXPIRED_KEY = "message"
TOKEN_EXPIRED_VALUE = "Invalid Token"

API_ERROR_RESPONSES = {
    "ERR-USR-USERNOTFOUND": "user not found",
    "ERR-USR-INVALIDPASSWORDERROR": "password is not correct",
}

OD_READ_RETRY_TIME = 15
TOKEN_EXPRIATION = datetime.timedelta(minutes=15)
