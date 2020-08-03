import configparser

config = configparser.ConfigParser()
config.read('config.ini')

def test():
    user = config['DEV']['DEV_USER']
    password = config['DEV']['DEV_PASSWORD']
    print("user is: ", user)
    print("password is: ", password)
	
test()