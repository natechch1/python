from chef import chef
# this ChineseChef class is inherit from chef class
class ChineseChef(chef):
    
    def make_fried_rice(self):
        print("The Chinese Chef can make fantastic fried rice!!")
    
    # it can also overwrite the function exist in the parent class
    def make_special_dish(self):
        print("The Chinese Chef's special dish is DiSanXian.")

    