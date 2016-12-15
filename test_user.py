import requests
import json

class work_with_user(object):
    def create_user(self, header, data):
        self.header = {'Content-type': 'application/json'}
        self.data = {
            "id": 1,
            "username": "JohnSmith",
            "firstname": "John",
            "lastname": "Smith",
            "password": 123456,
            "userstatus": 0, #status of user login
            }
        request = requests.post('baseUrl', data=json.dumps(data))
        return request.json()

    def user_login(self): # change status to 1 if user has successfully login
        pass

    def user_logout(self): # change status to 0 for logout user
        pass

    def edit_user(self):
        pass

    def delete_user(self):
        pass

    def get_user(self):
        pass


if __name__ == '__main__':
