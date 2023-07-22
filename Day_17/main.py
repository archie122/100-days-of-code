class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        self.followers += 1
        user.following += 1

user_1 = User('001', 'John')
user_2 = User('002', 'Jane')

print(user_1.id , user_1.name)

user_1.follow(user_2)
print(user_1.followers, user_1.following)
