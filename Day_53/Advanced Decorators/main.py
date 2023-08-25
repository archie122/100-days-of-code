class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticated(function):
    def wrapper(*args):
        if args[0].is_logged_in:
            function(args[0])
        else:
            print("You must be logged in to access this page.")

    return wrapper


@is_authenticated
def create_blog_post(user):
    print(f"The user {user.name} has created a new blog post!")


new_user = User("Archie")
new_user.is_logged_in = True
create_blog_post(new_user)
