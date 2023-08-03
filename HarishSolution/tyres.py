from dataclasses import dataclass

@dataclass 
class Tyres:
    wear: list = [0,0,0,0]

@dataclass
class CarriganTyres(Tyres):

    def needs_service(self):
        for i in self.wear:
            if i>0.9:
                return True
            
@dataclass
class OctoprimeTyres(Tyres):

    def needs_service(self):
        sum=0
        for i in self.wear:
            sum+=i
        if sum>3:
            return True