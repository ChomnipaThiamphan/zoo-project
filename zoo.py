class Zoo:
    def get_ticket_price(self, age):
        if 0 <= age <= 12:
            return 50
        elif 13 <= age <= 20:
            return 100
        elif 21 <= age <= 60:
            return 150
        elif age > 60:
            return 100

if __name__ == "__main__":
    zoo = Zoo()
    ages = [-10, 7, 19, 59, 75]
    for age in ages:
        price = zoo.get_ticket_price(age)
        print(f"The ticket price for age {age} is {price}")
        