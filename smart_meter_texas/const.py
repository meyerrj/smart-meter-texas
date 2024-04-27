import datetime

BASE_HOSTNAME = "www.smartmetertexas.com"
BASE_URL = "https://" + BASE_HOSTNAME
BASE_ENDPOINT = BASE_URL 
AUTH_ENDPOINT = "/commonapi/user/authenticate"
LATEST_OD_READ_ENDPOINT = "/api/usage/latestodrread"
METER_ENDPOINT = "/api/meter"
OD_READ_ENDPOINT = "/api/ondemandread"
INTERVAL_SYNCH = "/api/adhoc/intervalsynch"

USER_AGENT_TEMPLATE = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/85.0.{BUILD}.{REV} Safari/537.36"
)
CLIENT_HEADERS = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "origin": "https://www.smartmetertexas.com",
    "pragma": "no-cache",
    "referer": "https://www.smartmetertexas.com/home",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
}

API_ERROR_KEY = "errormessage"
TOKEN_EXPIRED_KEY = "message"
TOKEN_EXPIRED_VALUE = "Invalid Token"

API_ERROR_RESPONSES = {
    "ERR-USR-USERNOTFOUND": "user not found",
    "ERR-USR-INVALIDPASSWORDERROR": "password is not correct",
}
API_DATE_ERROR = "No Energy Data received from the respective TDSP"

OD_READ_RETRY_TIME = 15
TOKEN_EXPRIATION = datetime.timedelta(minutes=15)
