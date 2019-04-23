import web
render = web.template.render('./templates/')
urls = ("/.*", "hello")
app = web.application(urls, globals())


# Requests lib should be installed: http://docs.python-requests.org/en/master/user/install/#install
import requests

API_ENDPOINT = "https://dnxr7vm27d.execute-api.us-east-1.amazonaws.com/prod/GetRewardInfo"
API_KEY = "kE2xi2OgUa7jfijmsd0jQ74aJntJwUEW2EU8LUsi" # Your API key here
headers = {"x-api-key": API_KEY, "Content-Type": "application/json"} # Headers
# Data to be sent to API
data = {
    'appId': 'DEMO1',
    'momentId': 'GAME_COMPLETE',
    'deviceType': 'Android',
    'campaignId': 'DEMOCAMP1',
    'rewardGroupId': 'amz1yprime'
}
# Sending post request and saving response as response object
r = requests.post(url = API_ENDPOINT, headers=headers, json = data)
# extracting response text
response = r.text



class hello:
    def GET(self):
        name = 'Bob'
        return render.index(response)

if __name__ == "__main__":
    app.run()


