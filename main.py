import random
from termcolor import colored
from read_from_file import add_to_set

class Lottery:
    def add_customers_to_set(self):
        self.customers_with_points = add_to_set()
    
    def create_list_of_chances(self):
        self.participant_list = []
        for customer, chances in self.customers_with_points:
            for chance in range(0, chances):
                self.participant_list.append(customer)
        return self.participant_list
    
    def get_random_numbers(self):
        self.participant_list = self.create_list_of_chances()
        for i in range(0,2):
            print(colored(self.participant_list, 'red'))
            winner = random.choice(self.participant_list)
            print('winner is', colored(winner, 'green'))
            while(True):
                if winner in self.participant_list:
                    self.participant_list.remove(winner)
                else:
                    break

first = Lottery()
first.add_customers_to_set()
first.create_list_of_chances()
first.get_random_numbers()
