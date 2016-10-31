# https://kite.zerodha.com/connect/login?api_key=4slvsk0ov1w0zgvk

from kiteconnect import KiteConnect
import hashlib

				# Compute the SHA-256 checksum.
				api_key = "xxxx"
				api_secret = "yyyy"

				# Comes from the redirect parameters.
				request_token = "zzzz"

				h = hashlib.sha256(api_key + request_token + api_secret)
				checksum = h.hexdigest()

kite = KiteConnect(api_key="your_api_key")

# Redirect the user to the login url obtained
# from kite.login_url(), and receive the request_token
# from the registered redirect url after the login flow.
# Once you have the request_token, obtain the access_token
# as follows.

data = kite.request_access_token("request_token_here", secret="your_secret")
kite.set_access_token(data["access_token"])

# Place an order
try:
    order_id = kite.order_place(tradingsymbol="INFY",
                    exchange="NSE",
                    transaction_type="BUY",
                    quantity=1,
                    order_type="MARKET",
                    product="NRML")

    print("Order placed. ID is", order_id)
except Exception as e:
    print("Order placement failed", e.message)

# Fetch all orders
print(kite.orders())

