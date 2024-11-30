#class of bird, then subclasses "waterbird", "raptor", "songbird", "other"
#this app only proposes to identify some few specific birds, whose dictionaries are listed here on top

crane = {'back color': 'white', 'breast color': 'white', 'bill size': 'long', 'leg length': 'long', 'call complexity': 'simple', 'water type': 'fresh'}

#Bird class set with basic bird attributes common to all four subclasses, and their variable set at set_attributes()
#basic Bird dictionary variable set on this class as well
class Bird():
    def __init__(self):
        self.bird_type = None
    def set_bird_type(self, bird_type):
        self.bird_type = bird_type

    def __init__(self):
        super().__init__()
        self.back_color = None
        self.breast_color = None
        self.bill_size = None
        self.leg_length = None
        self.call_complexity = None


    def set_attributes(back_color, breast_color, bill_size, leg_length, call_complexity):
        back_color = back_color
        breast_color = breast_color
        bill_size = bill_size
        leg_length = leg_length
        call_complexity = call_complexity

        Bird.bird_dictionary = {'back color': back_color, 'breast color': breast_color, 'bill size': bill_size, 'leg length': leg_length, 'call complexity': call_complexity}

#tried to set waterbird as a test and demo, that adds water type since it is specific to waterbirds.
#waterbird dictionary is defined by this specific attribute. Updated basic bird dictionary to merge with waterbird 'water-type' dictionary
class Waterbird(Bird):
    def __init__(self):
        super().__init__()
        self.water_type = None
    def set_waterbird_attributes(self, water_type):
        self.water_type = water_type

        self.waterbird_dictionary = {'water type': water_type}
        self.bird_dictionary.update(self.waterbird_dictionary)
    
    
class Raptor(Bird):
    pass


class Songbird(Bird):
    pass

class Other(Bird):
    pass

#each subclass gets its variable. User inputs what type subclass and the basic attributes, all set in the basic bird_dictionary

def main():
    waterbird = Waterbird()
    raptor = Raptor()
    songbird = Songbird()
    other = Other()

    bird_type = input("What type of bird? - waterbird, raptor, songbird, or other? \n")

    print("Bird type is ", bird_type, "\n")

    back_color = input("What is back color? ")
    breast_color = input("What is breast color? ")
    bill_size = input("What is bill size? ")
    leg_length = input("What is leg length? ")
    call_complexity = input("What is call complexity? ")
    Bird.set_attributes(back_color, breast_color, bill_size, leg_length, call_complexity)

    print(Bird.bird_dictionary)

#if-else set specifically for waterbird type, where User inputs the added waterbird attribute, which gets added to basic bird dictionary as per before.
#if this basic waterbird bird_dictionary matches the contents of a bird's dictionary listed at the top of this app, it prints this info. Otherwise, unknown.
    if (bird_type == 'waterbird'):       

        water_type = input("What is water type? ")
        waterbird.set_waterbird_attributes(water_type)
        
        print(waterbird.bird_dictionary)
        
        if (waterbird.bird_dictionary == crane):
            print("Bird is crane.")
        else:
            print("Bird is unknown.")

    else:
        print("App still under construction.")

if __name__== "__main__":

    main()


