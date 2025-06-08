from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash

client = MongoClient("mongodb://localhost:27017/")
db = client["CardioInsight"]
users = db["Users"]

def insert_user(username, password, email):
    if users.find_one({"email": email}):
        return False  # Email already exists
    if users.find_one({"username": username}):
        return False  # Username already exists
    hashed_pw = generate_password_hash(password)
    users.insert_one({"username": username, "password": hashed_pw, "email": email})
    return True

def find_user(username, password):
    user = users.find_one({"username": username})
    if user and check_password_hash(user["password"], password):
        return user
    return None

def find_user_by_email(email):
    return users.find_one({"email": email})

def update_password_by_email(email, new_password):
    hashed_pw = generate_password_hash(new_password)
    result = users.update_one({"email": email}, {"$set": {"password": hashed_pw}})
    return result.modified_count > 0