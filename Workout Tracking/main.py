import requests
import pprint

cities = ["Paris",
          "Berlin",
          "Tokyo",
          "Sydney",
          "Istanbul",
          "Kuala Lumpur",
          "New York",
          "San Francisco",
          "Cape Town"]

end_point = "https://tequila-api.kiwi.com/locations/query"

apikey = "sSv5JKTl8Ez18-1LfsSkorqWKWvdrP5P"

headers = {"apiKey": apikey}

for city in cities:

    body = {"term": city}

    response = requests.get(url=end_point, params=body, headers=headers)

    data = response.json()

    # pprint.pprint(data)

    print(data["locations"][0]["code"])