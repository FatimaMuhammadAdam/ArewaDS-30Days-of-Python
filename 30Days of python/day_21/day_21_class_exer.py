import statistics
class Statistics:
    def _init_( self, sample):
        self.sample = sample
    def mean(self):
        return statistics.mean(self.sample)
    def meadian(self):
        return statistics.median(self.sample)
    def mode(self):
        return statistics.mode(self.sample)
    def range(self):
        try:
           return statistics.range(self.sample)
        except statistics.Statisticserror:
           return None
    def variance(self):
        return statistics.variance(self.sample)
    
    def stdev(self):
        return statistics.stdev(self.sample)
    
    def min(self):
        return min(self.sample)
    
    def max(self):
        return max(self.sample)
    
    def count(self):
        return len(self.sample)
    
    def percentile(self, p):
        return statistics.quantiles(self.sample, n=100)[p]
    
    def freq_distribution(self):
        freq = {}
        for x in self.sample:
            if x in freq:
                freq[x] += 1
            else:
                freq[x] = 1
        return freq
sample = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
stats = Statistics(sample)

print(stats.mean())
print(stats.median())
print(stats.mode())
print(stats.range())
print(stats.variance())
print(stats.stdev())
print(stats.min())
print(stats.max())
print(stats.count())
print(stats.percentile(50))
print(stats.freq_distribution())(sample)


class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = {}
        self.expenses = {}

    def add_income(self, description, amount):
        if description in self.incomes:
            self.incomes[description] += amount
        else:
            self.incomes[description] = amount

    def add_expense(self, description, amount):
        if description in self.expenses:
            self.expenses[description] += amount
        else:
            self.expenses[description] = amount

    def total_income(self):
        return sum(self.incomes.values())

    def total_expense(self):
        return sum(self.expenses.values())

    def account_info(self):
        print(f"Name: {self.firstname} {self.lastname}")
        print(f"Total income: {self.total_income()}")
        print(f"Total expenses: {self.total_expense()}")
        print(f"Account balance: {self.account_balance()}")

    def account_balance(self):
        return self.total_income() - self.total_expense()

person = PersonAccount("AISHA", "MUHAMMAD ADAM")
person.add_income("Salary", 10000)
person.add_income("Bonus", 1000)
person.add_expense("Rent", 1000)
person.add_expense("SARKA", 500)
person.account_info()
