class FancyFoodOrder:
    def __init__(self, food, amount):
        self.__food_name = ""
        self.__amount_in_pounds = 0.0
        self.__standard_price_per_pound = 0.0
        self.__calculated_price = 0.0

        self.__initialize(food, amount)

    def __initialize(self, food, amount):
        self.__food_name = food
        self.__amount_in_pounds = amount
        self.__set_standard_price()
        self.__calculate_price()

    def __set_standard_price(self):
        def PriceList(self):
            if self.__food_name == 'Dry Cured Iberian Ham':
                self.__standard_price_per_pound = 177.80
            elif self.__food_name == 'Wagyu Steaks':
                self.__standard_price_per_pound = 450.00
            elif self.__food_name == 'Matsutake Mushrooms':
                self.__standard_price_per_pound = 0.00  
            elif self.__food_name == 'Kopi Luwak Coffee':
                self.__standard_price_per_pound = 272.00
            elif self.__food_name == 'Moose Cheese':
                self.__standard_price_per_pound = 487.20
            elif self.__food_name == 'White Truffles':
                self.__standard_price_per_pound = 3600.00
            elif self.__food_name == 'Blue Fin Tuna':
                self.__standard_price_per_pound = 3603.00
            elif self.__food_name == 'Le Bonnotte Potatoes':
                self.__standard_price_per_pound = 270.81
            else:
                self.__standard_price_per_pound = 0.00

        PriceList(self) 

    def __calculate_price(self):
        self.__calculated_price = self.__amount_in_pounds * self.__standard_price_per_pound

    def calculate_cost(self):
        return self.__calculated_price

    def get_food_name(self):
        return self.__food_name

    def get_amount_in_pounds(self):
        return self.__amount_in_pounds

    def get_standard_price_per_pound(self):
        return self.__standard_price_per_pound

    def __str__(self):
        return f"Food: {self.__food_name}, Amount: {self.__amount_in_pounds} lbs, " \
               f"Standard Price per Pound: ${self.__standard_price_per_pound:.2f}, " \
               f"Calculated Price: ${self.__calculated_price:.2f}"