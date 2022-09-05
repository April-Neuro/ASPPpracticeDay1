import json

def get_credentials():

    username = input('Enter your username: ')
    password = input(f"Enter your password: ")
    
    return username, password

def read_passwdb(passwd):
    with open('passwd.json', 'r') as pwdb_file:
        jpwdb = json.load(pwdb_file)

def write_passwdb(passwd):
    with open('passwd.json', 'w') as pwdb_file:
        json.dump(pwdb, pwdb_file)
        
def add_user(pwdb, username, password):
    if username not in pwdb:
        pwdb[username] = password
    return
        
def authenticate(username, password, pwdb):
    if username in pwdb:
        if password == pwdb[username]:
            return True
        else:
            return False
    else:
        add_user(pwdb, username, password)
        return True

def main():
    username, password = get_credentials()
    pwdb = read_passwdb()
    status = authenticate(username, password, pwdb)
    if status:
        print("Success!")
    else:
        print("Wrong username or password!")
    write_passwdb(pwdb)
        
if __name__ == '__main__':
    username, password = get_credentials()
    pwdb = {username:password}
    write_passwdb(pwdb)
    

