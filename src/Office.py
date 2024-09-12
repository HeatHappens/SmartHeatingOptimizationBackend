from src.heating import Heating

class Office:
    def __init__(self, heating, volume, wall_area, window_area, roof_area, u_wall, u_window, u_roof):
        self.volume: float = volume
        self.heating: Heating = heating
        
        self.wall_area = wall_area
        self.window_area = window_area
        self.roof_area = roof_area
        self.u_wall = u_wall
        self.u_window = u_window
        self.u_roof = u_roof
    

    def compute_loss_power(self, inside_temperature, outside_temperature):
        delta_T = inside_temperature - outside_temperature
        
        # Calculate heat loss for each component
        heat_loss_walls = self.u_wall * self.wall_area * delta_T
        heat_loss_windows = self.u_window * self.window_area * delta_T
        heat_loss_roof = self.u_roof * self.roof_area * delta_T
        
        # Total heat loss
        return heat_loss_walls + heat_loss_windows + heat_loss_roof
    
    def compute_next_temperature(self, insideTemperature, outsideTempearature, energyConsumption, number_of_people = 0):
        heat_gain_from_people = number_of_people * 120 #Average value
        Q = self.heating.compute_heat_power(energyConsumption, insideTemperature) - self.compute_loss_power(insideTemperature, outsideTempearature) + heat_gain_from_people
        m = self.volume * 1.2
        deltaT = Q / (m * 1005)
        return insideTemperature + deltaT
    