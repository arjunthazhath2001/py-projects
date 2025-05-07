import requests

pixela_url= "https://pixe.la/v1/users"

params={
    "token":"etet90kcnal",
    "username":"arjunta",
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}


response= requests.post(url=pixela_url,json=params)

print(response.text)