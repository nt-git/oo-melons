"""Classes for melon orders."""


class AbstractMelonOrder(object):
    """An abstract base class that other Melon Orders inherit from"""

    def __init__(self, species, qty, country_code=None, passed_inspection=False):
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

        if self.species == "Christmas melons":
            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price

        return total


    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True
        # moved from DomesticMelonOrder


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    tax = .08
    order_type = "domestic"


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):

        self.country_code = country_code
        self.tax = 0.17
        self.order_type = "international"
        self.species = species # added species for part 2
        self.qty = qty # added qty for part 2
        # this has to be self because it's in the __init__
        # ...and therefore is on the object, not the class

    def get_country_code(self):
        """Return the country code."""
        #method on the class InternationalMelonOrder

        return self.country_code
        # international has country code; domestic does not
        # WAI???

    def get_total(self):
        """Fee calculation for int'l order"""

        subtotal = super(InternationalMelonOrder, self).get_total()
        if self.qty < 10:
            total = subtotal + 3

        return total


class GovernmentMelonOrder(AbstractMelonOrder):
    """No tax for all gov't orders"""

    # what is specific to this class?
    def __init__(self, species, qty, country_code, passed_inspection):

        self.passed_inspection = False
        self.tax = 0

    def mark_inspection(self):
        """Record the fact than an order has been shipped."""

        self.passed_inspection = True

    def get_total(self):
        """Not tax for gov't orders"""
        subtotal = super(GovernmentMelonOrder, self).get_total()

        total = self.qty * base_price

        return total