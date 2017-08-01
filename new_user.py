from common.database import Database

Database.initialize()
Database.insert('user', {"email": "ee@test.com", "password": "123456"})
user = Database.find_one('user', {"email": "ee@test.com"})
print(user)
