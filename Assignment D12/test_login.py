def login(username, password):
    if username == "admin" and password == "admin123":
        return "Login Successful"
    return "Login Failed"

def test_valid_login():
    result = login("admin", "admin123")
    assert result == "Login Successful"

def test_invalid_login():
    result = login("user", "wrongpassword")
    assert result == "Login Failed"