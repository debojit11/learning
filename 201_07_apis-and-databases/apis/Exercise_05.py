'''
Write a program that makes a DELETE request to remove the user your create in a previous example.

Again, make a GET request to confirm that information has been deleted.

'''
import requests

url = "http://demo.codingnomads.co:8080/tasks_api/users"
response = requests.delete(url + "/6925")
print(response.status_code)