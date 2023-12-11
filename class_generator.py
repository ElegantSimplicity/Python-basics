class DivisibleBySeven:
    '''
    Define a class with a generator which can iterate the numbers,
    which are divisible by 7, between a given range 0 and n.
    '''    
    def __init__(self,n):
        self.n = n
    
    def generate_divisible_by_seven(self):
        for num in range(self.n + 1):
            if num % 7 == 0:
                yield num

n = int(input("Enter your desired range: "))

# Call the method to start the generator
generator = DivisibleBySeven(n).generate_divisible_by_seven()

# Iterate through the generated numbers
for num in generator:
  print(num)    
