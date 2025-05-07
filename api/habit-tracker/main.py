import requests
import datetime

pixela_url= "https://pixe.la/v1/users"
USERNAME="arjunta"
TOKEN= "etet90kcnal"

GRAPH_ID="cycling1"

params={
    "token": TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}


# response= requests.post(url=pixela_url,json=params)

# print(response.text)


graph_endpoint= f"{pixela_url}/{USERNAME}/graphs"

params={
    "id":"cycling1",
    "name":GRAPH_ID,
    "unit":"km",
    "type":"float",
    "color":"ichou"
}

headers={
    "X-USER-TOKEN":TOKEN
}


# response=requests.post(url=graph_endpoint,json=params,headers=headers)

# print(response.text)


pixel_post_endpoint= f"{graph_endpoint}/{GRAPH_ID}"


today= datetime.datetime.now().strftime("%Y%m%d")


post_params={
    "date":today,
    "quantity": input("HOw much")
}


response= requests.post(url=pixel_post_endpoint,json=post_params,headers=headers)
print(response.text)



# pixel_put_delete_endpoint= f"{pixel_post_endpoint}/{today}"

# put_params={
#     "quantity":'100000'
# }

# response= requests.put(url=pixel_put_delete_endpoint,json=put_params,headers=headers)
# print(response.text)



# response= requests.delete(url=pixel_put_delete_endpoint,headers=headers)

# print(response.text)