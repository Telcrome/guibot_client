PRODUCTION = True

if PRODUCTION:
    WEB_ADDRESS = "open-bot-server.herokuapp.com/"
else:
    WEB_ADDRESS = "localhost:8080/"

REMOTE_HTTP = f"https://{WEB_ADDRESS}"
REMOTE_WS = f"wss://{WEB_ADDRESS}"
