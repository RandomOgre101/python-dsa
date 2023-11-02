# QUESTION 1: As a senior backend engineer at Jovian, you are tasked with developing a fast in-memory data structure
# to manage profile information (username, name and email) for 100 million users.
# It should allow the following operations to be performed efficiently:
# Insert the profile information for a new user.
# Find the profile information of a user, given their username
# Update the profile information of a user, given their usrname
# List all the users of the platform, sorted by username
# You can assume that usernames are unique.


class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email

    def introduce_yourself(self, guest_name):
        print(f"Hi {guest_name}, I'm {self.name}! Contact me at {self.email}")


user2 = User('john', 'John Doe', 'john@doe.com')


class UserDatabase:
    def __init__(self):
        self.users = []

    def insert(self, user):
        i = 0
        while i < len(self.users):
            if self.users[i].username > user.username:
                break
            i += 1
        self.users.insert(i, user)

    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user

    def update(self, user):
        target = self.find(user.username)
        target.name, target.email = user.name, user.email

    def list_all(self):
        return self.users


aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')

users = [aakash, biraj, hemanth, jadhesh, siddhant, sonaksh, vishal]
rishi = User('rishi', 'Rishikeshav', 'r@gmail.com')

ub = UserDatabase()
ub.insert(rishi)
