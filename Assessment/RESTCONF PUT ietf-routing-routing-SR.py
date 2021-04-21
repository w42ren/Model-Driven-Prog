import json
import requests
requests.packages.urllib3.disable_warnings()

api_url = "https://192.168.56.3/restconf/data/ietf-routing:routing"

headers = { "Accept": "application/yang-data+json", 
            "Content-type":"application/yang-data+json"
          }

basicauth = ("cisco", "cisco123!")

yangConfig ={
    "ietf-routing:routing": {
        "routing-instance": [
            {
                "name": "default",
                "description": "default-vrf [read-only]",
                "routing-protocols": {
                    "routing-protocol": [
                        {
                            "type": "ietf-routing:static",
                            "name": "1",
                            "static-routes": {
                                "ietf-ipv4-unicast-routing:ipv4": {
                                    "route": [
                                        {
                                            "destination-prefix": "2.2.2.0/24",
                                            "next-hop": {
                                                "outgoing-interface": "GigabitEthernet2"
                                            }
                                        }
                                    ]
                                }
                            }
                        }
                    ]
                }
            }
        ]
    }
}


resp = requests.put(api_url, data=json.dumps(yangConfig), auth=basicauth, headers=headers, verify=False)
if(resp.status_code >= 200 and resp.status_code <= 299):
    print("STATUS OK: {}".format(resp.status_code))
else:
    print("Error code {}, reply: {}".format(resp.status_code, resp.json()))
