import os
import sys
import time

PATH_TO_ADD = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
if PATH_TO_ADD not in sys.path:
    sys.path.append(PATH_TO_ADD)

from wazirx_sapi_client.rest import Client

# Keys for private events
api_key = "test_api_key"
secret_key = "test_secret_key"

# public
c = Client()


#print(type(c.send("ping")))
#print(type(c.send("time")))
#print(type(c.send("system_status")))
#print(type(c.send("exchange_info")))


print(c.send("ping"))
time=c.send("time")
print(time[0])
t=time[1]
print(t)

from timeconvert import time
tm= tim(t)
print(tm)
