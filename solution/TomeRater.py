class User(object):
    def __init__(self, name, email):

        try:
            if email[-3:].find("com") != -1 or email[-3:].find("org") != -1 or email[-3:].find("edu") != -1 and email.find("@") != -1:
                self.email = email
                self.name = name
                self.books = {}
            else:
                raise NameError("sorry, email not valid")
        except NameError:
            print("The email address {} is not valid, try again".format(email))
            quit()



    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("email was replaced successfully")

    def __repr__(self):
        return "User {}, email:{}, books read: {}".format(self.name, self.email, len(self.books))

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return True

    def read_book(self, book, rating=None):
            self.books[book] = rating

    def get_average_rating(self):
        total = 0
        count_none = 0
        for rating in self.books.values():
            if rating is not None:
                total += rating
            else:
                count_none += 1
        average = total/(len(self.books)-count_none)

        return average


class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, isbn):
        self.isbn = isbn
        print("ISBN was updated")

    def add_rating(self, rating):
        if rating in range(5):
            self.ratings.append(rating)
        else:
            return "Invalid Rating"

    def __repr__(self):
        return str(self.title)

    def __eq__(self,other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            return True

    def get_average_rating(self):
        total = 0
        for rating in self.ratings:
            total += rating
        average = total/len(self.ratings)
        return average

    def __hash__(self):
        return hash((self.title, self.isbn))


class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return str(self.title) + " by " + str(self.author)


class NonFiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{}, a {} manual on {}".format(self.title, self.level, self.subject)


class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}
        self.isbn = []

    def create_book(self, title, isbn):
        if isbn in self.isbn:
            print("Similar ISBN {} already exists for a different book. Use a different ISBN number and try again".format(isbn))
            quit()
        else:
            book = Book(title, isbn)
            self.isbn.append(isbn)
            return book

    def create_novel(self, title, author, isbn):
        if isbn in self.isbn:
            print("Similar ISBN {} already exists for a different book. Use a different ISBN number and try again".format(isbn))
            quit()
        else:
            fiction_book = Fiction(title, author, isbn)
            self.isbn.append(isbn)
            return fiction_book


    def create_non_fiction(self, title, subject, level, isbn):
        if isbn in self.isbn:
            print("Similar ISBN {} already exists for a different book. Use a different ISBN number and try again".format(isbn))
            quit()
        else:
            non_fiction_book = NonFiction(title, subject, level, isbn)
            self.isbn.append(isbn)
            return non_fiction_book

    def add_book_to_user(self, book, email, rating=None):
        if email in self.users:
            self.users[email].read_book(book, rating)
            book.add_rating(rating)
            if book not in self.books.keys():
                self.books[book] = 1
            else:
                self.books[book] += 1
        else:
            print("No user with email {}!".format(email))

    def add_user(self, name, email, user_books=None):
        if email in self.users.keys():
            print("A user with email {} already exists. Try with a different email address".format(email))
            quit()
        else:
            user = User(name, email)
            self.users[email] = user

        if user_books is not None:
            for book in user_books:
                self.add_book_to_user(book, email)
                self.books[book] = 1

    def print_catalog(self):
        for book in self.books.keys():
            print(book)

    def print_users(self):
        for user in self.users.values():
            print(user)

    def most_read_book(self):
        maxi = 0
        for book in self.books.keys():
            if self.books[book] > maxi:
                maxi = self.books[book]
                top = book
        return top

    def highest_rated_book(self):
        average_rating = 0
        for book in self.books.keys():
            if book.get_average_rating() > average_rating:
                average_rating = book.get_average_rating()
                top_book = book

        return top_book

    def most_positive_user(self):
        best_rating = 0
        for user in self.users.values():
            if user.get_average_rating() > best_rating:
                best_rating = user.get_average_rating()
                best_user = user

        return best_user

    def __repr__(self):
        lst1 = list(self.users.keys())
        lst2 = list(self.books.keys())
        return "The users:" + str(lst1) + " , books rated: " + str(lst2)

    def __eq__(self,other_tome_rater):
        if self.users == other_tome_rater.users and self.books == other_tome_rater.books:
            return True


