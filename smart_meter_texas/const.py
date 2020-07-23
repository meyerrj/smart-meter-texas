BASE_URL = "https://www.smartmetertexas.com/"
BASE_ENDPOINT = BASE_URL + "api"
AUTH_ENDPOINT = "/user/authenticate"
DASHBOARD_ENDPOINT = "/dashboard"
OD_READ_ENDPOINT = "/ondemandread"
LATEST_OD_READ_ENDPOINT = "/usage/latestodrread"

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14;"
    "rv:77.0) Gecko/20100101 Firefox/77.0"
)

API_ERROR_KEY = "errormessage"
TOKEN_EXPIRED_KEY = "message"
TOKEN_EXPIRED_VALUE = "Invalid Token"

API_ERROR_RESPONSES = {
    "ERR-USR-USERNOTFOUND": "user not found",
    "ERR-USR-INVALIDPASSWORDERROR": "password is not correct",
}

OD_READ_RETRY_TIME = 15
