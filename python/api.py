import requests

class Api:
    baseurl=('https://jsonplaceholder.typicode.com')
    def getbyid(self,path, id):
        response=requests.get(f'{self.baseurl}{path}/{id}')
        return response.json()
    
    def get_all(self,path):
        response=requests.get(f'{self.baseurl}{path}')
        return response.json()



import requests
response=requests.get('https://jsonplaceholder.typicode.com/posts/30') 
print(response.json())
