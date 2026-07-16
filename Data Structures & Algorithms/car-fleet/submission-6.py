class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # Stack depends on the car with the further position
        resStack = []   
        cars = []

        # Sorting might help solving this problem easier
        # Map approach didn't work so we will use a Class
        class Car:
            def __init__(self, pos: int, spe: int):
                self.pos = pos
                self.spe = spe

        for i in range(len(position)):
            cars.append(Car(position[i], speed[i]))

        sorted_cars = sorted(cars, key=lambda car: car.pos)
        
        
        '''
        Once they are sorted:
        - Calculate the difference between position, keys and velocity
        '''
        def turns(t: int, c: Car) -> int:
            rem = t - c.pos
            return rem / c.spe


        for i in range(len(sorted_cars) -1, -1, -1):
            temp = turns(target, sorted_cars[i])

            if len(resStack) == 0:
                resStack.append((temp, sorted_cars[i]))
                continue
            
            if temp > resStack[-1][0]:
                resStack.append((temp, sorted_cars[i]))
            elif temp == resStack[-1][0]:
                if (sorted_cars[i].pos + (sorted_cars[i].spe * temp) < resStack[-1][1].pos + (resStack[-1][1].spe * temp)):
                    resStack.append((temp, sorted_cars[i]))
            

            
        return len(resStack)
            