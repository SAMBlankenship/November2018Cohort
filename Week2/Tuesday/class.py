class Person: 
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0
        self.greeting_list = []

    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name, self.name))
        self.greeting_count += 1
        if other_person in self.greeting_list:
            pass
        else:
            self.greeting_list.append(other_person)
    
    def print_contact_info(self):
        print("{0}'s email: {1}, {0}'s phone number: {2}".format(self.name, self.email, self.phone))

    def add_friend(self, friend):
        self.friends.append(friend)
    
    def num_friends(self):
        return len(self.friends)
    
    def num_unique_people_greeted(self):
        print(len(self.greeting_list))

    def ListOfPeople(self):
        for p in self.greeting_list:
            print(p.name)

    def __str__(self):
        return 'Person: {} {} {}'.format(self.name, self.email, self.phone)

sonny = Person("Sonny", 'sonny@hotmail.com', '483-485-4948')
jordan = Person("Jordan", 'jordan@aol.com', '495-586-3456')
dee_ann = Person("deann", 'me@me.com', '333-333-3333')

sonny.greet(jordan)
# sonny.num_unique_people_greeted() 

# sonny.greet(jordan) 
# sonny.num_unique_people_greeted()

sonny.greet(dee_ann) 
sonny.greet(sonny)
# sonny.num_unique_people_greeted()

# jordan.greet(sonny)
# sonny.num_unique_people_greeted()

# sonny.num_unique_people_greeted() 

# print(sonny.greeting_list[1].name)

sonny.ListOfPeople()

