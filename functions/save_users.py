def save_user(**user):
    print(user)
    print(user['id'])
    print(user['name'])


save_user(id=1, name="Tobi", age=22)