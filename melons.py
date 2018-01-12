"""Classes for melon orders."""

class AbstractMelonOrder(object):
    """An abstract base class that other Melon Orders inherit from"""

    def __init__(self, species, qty, country_code = None):
        """Initialize melon order attributes."""
        # creates the instance
        self.species = species
        self.qty = qty
        self.shipped = False
        if country_code:
            self.country_code = country_code
        # if country code isn't none or false, will set country code attribute
        # ...as entered country code

    def get_total(self):
        """Calculate price, including tax."""
        # method on the class DomesticMelonOrder

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price

        return total
        # moved from DomesticMelonOrder

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""
        # method on the class DomesticMelonOrder

        self.shipped = True
        # moved from DomesticMelonOrder


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    tax = .08
    order_type = "domestic"


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    # def __init__(self, species, qty, country_code):
    #     """Initialize melon order attributes."""
    #     # creates the instance

    #     self.species = species
    #     self.qty = qty
    #     self.country_code = country_code
    #     self.shipped = False
    #     self.order_type = "international"
    #     self.tax = 0.17
    tax = 0.17
    order_type = "international"

    def get_country_code(self):
        """Return the country code."""
        #method on the class InternationalMelonOrder

        return self.country_code
