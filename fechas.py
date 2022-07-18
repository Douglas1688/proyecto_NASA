# import requests

# url = "https://verificationapi-v1.sinch.com/verification/v1/verifications"
# payload="{\n  \"identity\": {\n  \"type\": \"number\",\n  \"endpoint\": \"+593980077903\"\n  },\n  \"method\": \"sms\"\n}"
# headers = {
#   'Content-Type': 'application/json',
#   'Authorization': 'Basic YmFhMmM4ZDctMGQxYy00YWU3LTllYjQtZjIzOTlmMTA1OThkOk1DNU0zTjJ1a1VXZkJzbFlKcFV5bGc9PQ=='
# }
# response = requests.request("POST", url, headers=headers, data=payload)

# print(response.json())

from datetime import datetime, timedelta
ahora = datetime.now().strftime("%Y-%m-%d")
hace_5 = datetime.now() - timedelta(days=5)

print("{} - {}".format(ahora, hace_5.strftime("%Y-%m-%d")))