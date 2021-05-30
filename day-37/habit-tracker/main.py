# https://docs.pixe.la/
import requests
import datetime as dt


def create_user_account():
    pixela_endpoint = "https://pixe.la/v1/users"
    parameters = {
        "token": "qhqj0q73252f2f2",
        "username": "lhserafim",
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }
    response = requests.post(pixela_endpoint, json=parameters)
    response.raise_for_status()
    print(response.text)
    # https://pixe.la/@lhserafim


def create_graph_definition(username: str, password: str):
    pixela_endpoint = f"https://pixe.la/v1/users/{username}/graphs"

    # Request Header
    header = {
        "X-USER-TOKEN": password
    }

    parameters = {
        "id": "graph1",
        "name": "Studies",
        "unit": "hours",
        "type": "float",
        "color": "shibafu"
    }
    response = requests.post(pixela_endpoint, json=parameters, headers=header)
    response.raise_for_status()
    print(response.text)


def post_a_pixel(username: str, password: str, graph_id: str):
    pixela_endpoint = f"https://pixe.la/v1/users/{username}/graphs/{graph_id}"

    # Request Header
    header = {
        "X-USER-TOKEN": password
    }

    # Formatação de data: https://www.w3schools.com/python/python_datetime.asp
    parameters = {
        "date": dt.date.today().strftime("%Y%m%d"),  # yyyyMMdd
        "quantity": "2"
    }

    response = requests.post(url=pixela_endpoint, json=parameters, headers=header)
    response.raise_for_status()
    print(response.text)


def update_a_pixel(username: str, password: str, graph_id: str, date: str, quantity: str):
    pixela_endpoint = f"https://pixe.la/v1/users/{username}/graphs/{graph_id}/{date}"

    header = {
        "X-USER-TOKEN": password
    }

    parameters = {
        "quantity": quantity
    }

    response = requests.put(url=pixela_endpoint, json=parameters, headers=header)
    response.raise_for_status()
    print(response.text)


def delete_a_pixel(username: str, password: str, graph_id: str, date: str, quantity: str):
    pixela_endpoint = f"https://pixe.la/v1/users/{username}/graphs/{graph_id}/{date}"

    header = {
        "X-USER-TOKEN": password
    }

    response = requests.delete(url=pixela_endpoint, headers=header)
    response.raise_for_status()
    print(response.text)


# create_user_account
# create_graph_definition("lhserafim", "qhqj0q73252f2f2")

# print(dt.date.today().strftime("%Y%m%d"))
post_a_pixel("lhserafim", "qhqj0q73252f2f2", "graph1")
update_a_pixel("lhserafim", "qhqj0q73252f2f2", "graph1", dt.date.today().strftime("%Y%m%d"), "2.20")
delete_a_pixel("lhserafim", "qhqj0q73252f2f2", "graph1", dt.date.today().strftime("%Y%m%d"), "2.20")
