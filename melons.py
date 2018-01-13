"""Classes for melon orders."""


class AbstractMelonOrder(object):
    """An abstract base class that other Melon Orders inherit from"""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        # creates the instance
        self.species = species
        self.qty = qty
        self.shipped = False
        # if country_code:
        #     self.country_code = country_code
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

    tax = 0.17
    order_type = "international"

    def __init__(self, species, qty, country_code):

        self.country_code = country_code
        super(InternationalMelonOrder, self).__init__(species, qty)
        # calling information on part AbstractMelon...
        # MRO - instance > class > talk to classes' parent class... etc.

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
    """Class for handling government orders"""

    tax = 0
    passed_inspection = False
    # what is specific to this class?

    def mark_inspection_results(self, passed):
        """Record the results of an order having been inspected."""

        self.passed_inspection = passed
