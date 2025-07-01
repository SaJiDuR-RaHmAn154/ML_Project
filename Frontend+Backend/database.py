from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash

client = MongoClient("mongodb://localhost:27017/")
db = client["CardioInsight"]
users = db["Users"]

def insert_user(username, password, email, profile_pic_url=None):
    if users.find_one({"email": email}):
        return False  # Email already exists
    if users.find_one({"username": username}):
        return False  # Username already exists
    users.insert_one({
        "username": username,
        "password": generate_password_hash(password),
        "email": email,
        "profile_pic_url": profile_pic_url
    })
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

def get_user_profile(username):
    return users.find_one({"username": username}, {"password": 0})

def add_checkup_history(username, input_data, result):
    from datetime import datetime
    users.update_one(
        {"username": username},
        {"$push": {"history": {
            "timestamp": datetime.utcnow().isoformat(),
            "input": input_data,
            "result": result
        }}}
    )

def get_checkup_history(username):
    user = users.find_one({"username": username}, {"history": 1})
    return user.get("history", []) if user else []

def delete_checkup_history(username, timestamp):
    users.update_one(
        {"username": username},
        {"$pull": {"history": {"timestamp": timestamp}}}
    )

def update_user_profile(current_username, new_username, new_email, profile_pic_url):
    update_fields = {}
    if new_username:
        update_fields["username"] = new_username
    if new_email:
        update_fields["email"] = new_email
    if profile_pic_url:
        update_fields["profile_pic_url"] = profile_pic_url
    if update_fields:
        users.update_one({"username": current_username}, {"$set": update_fields})