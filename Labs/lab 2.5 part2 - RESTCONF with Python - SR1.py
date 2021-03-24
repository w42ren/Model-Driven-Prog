import json
import requests
requests.packages.urllib3.disable_warnings()

api_url = "https://192.168.56.3/restconf/api/running/native/ip/route/"

headers = { "Accept": "application/yang-data+json", 
            "Content-type":"application/yang-data+json"
          }

basicauth = ("cisco", "cisco123!")

yangConfig ={
  "ned:route": {
    "ip-route-interface-forwarding-list":
    [
      {
        "prefix": "1.1.1.1",
        "mask": "255.255.255.255",
        "fwd-list": [
          {
            "fwd": "Loopback100"
          }
        ]
      },
      {
        "prefix": "2.2.2.2",
        "mask": "255.255.255.255",
        "fwd-list": [
          {
            "fwd": "Loopback101"
          }
        ]
       }
    ],

    "vrf":
    [
      {
        "name": "asd",
        "ip-route-interface-forwarding-list":
        [
          {
            "prefix": "1.1.1.1",
            "mask": "255.255.255.255",
            "fwd-list":
            [
              {
                "fwd": "Null0"
              }
            ]
          }
        ]
      }
    ]
  }
}
print(json.dumps(yangConfig))
resp = requests.put(api_url, data=json.dumps(yangConfig), auth=basicauth, headers=headers, verify=False)
if(resp.status_code >= 200 and resp.status_code <= 299):
    print("STATUS OK: {}")    #.format(resp.status_code))
else:
    print("Error code {}, reply: {}") #.format(resp.status_code, resp.json()))
