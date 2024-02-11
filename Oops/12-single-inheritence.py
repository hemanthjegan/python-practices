class Nokia:
    company = "Nokia india"
    website = "www.nokia.in"

    def contact_details(self):
        print("Address : cherry road, new bus stand, chennai.")

class Nokia1100(Nokia):  # inherits parent class
    def __init__(self):
        self.name="Nokia 1100"
        self.year = "1998"

    def prod_details(self):
        print("Name    : ", self.name)
        print("Year    : ", self.year)
        print("Company : ", self.company)
        print("Website : ", self.website)

mobile = Nokia1100()
mobile.prod_details()
mobile.contact_details()