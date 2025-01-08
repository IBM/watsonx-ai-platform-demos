# Bee Stack Example

![image](bee-stack-1.png)

![image](bee-stack-2.png)

```
import requests

def update_router(phoneNumber: str) -> dict:
  """
  Updates the software of routers remotely for a subscriber with a certain phone number.

  :param phoneNumber: Phone number of a subscriber, for example '123-456-7890'
  :return: whether update was successful
  """
  response = {
    success: "true",
    text: "Router has been updated"
  }
  return response.json()
```


You are an expert for router updates in customer care scenarios. Based on a transcript of a support call you determine whether a router update is necessary. If necessary, invoke the RouterUpdate tool to fix the router.