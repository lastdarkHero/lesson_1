import requests

response = requests.get("https://swapi.dev/api/")
data = response.json()

starships_url = data["starships"]


planets_response = requests.get(starships_url)


def get_starships_info(roof_url):

    starships_list = []
    new_starships_list = []
    

    for i in range(1,6):
        response = requests.get(f"{roof_url}/{i}")
        print(response.json())
        starships_list.append(int(response.json()["max_atmosphering_speed"]))
        new_starships_list.append(response.json())


    max_max_atmosphering_speed = max(starships_list)


    for starship in starships_list:
        if int(starship['max_name']) == max_max_atmosphering_speed:
            print(starship['name'])


   


    
