from abc import ABC, abstractmethod

class Heating(ABC):
    def __init__(self):
        self.efficiency_factor = 1.0  # Default efficiency factor

    @abstractmethod
    def carbon_costs(self, energy_consumption: float) -> float:
        """
        Calculate the carbon emissions based on the energy consumption.
        """
        pass
    
    @abstractmethod
    def compute_heat_power(self, energy_consumption: float, inside_temperature: float) -> float:
        """
        Calculate the heat power produced based on energy consumption and the current inside temperature.
        """
        pass


class GasHeating(Heating):
    def __init__(self):
        super().__init__()
        self.efficiency_factor = 0.9

    def carbon_costs(self, energy_consumption: float) -> float:
        """
        Calculate the carbon emissions based on the energy consumption.

        Args:
            energy_consumption (float): The amount of energy consumed in kWh.

        Returns:
            float: The carbon emissions in kg of CO2.
        """
        return energy_consumption * 0.184

    def compute_heat_power(self, energy_consumption: float, inside_temperature: float) -> float:
        """
        Calculate the heat power produced based on energy consumption and the current inside temperature.

        Args:
            energy_consumption (float): The energy consumed in kWh.
            inside_temperature (float): The current inside temperature in degrees Celsius.

        Returns:
            float: The heat power produced in kW.
        """
        # Power is calculated based on the efficiency factor (COP).
        return energy_consumption * self.efficiency_factor


class PumpHeating(Heating):
    def __init__(self, electricity_carbon_cost: float = 0.233):
        super().__init__()
        self.efficiency_factor = 3.5  # Adjusted COP
        self.electricity_carbon_cost = electricity_carbon_cost

    def carbon_costs(self, energy_consumption: float) -> float:
        """
        Calculate the carbon emissions based on the energy consumption.

        Args:
            energy_consumption (float): The amount of energy consumed in kWh.

        Returns:
            float: The carbon emissions in kg of CO2.
        """
        return energy_consumption * self.electricity_carbon_cost

    def compute_heat_power(self, energy_consumption: float, inside_temperature: float) -> float:
        """
        Calculate the heat power produced based on energy consumption and the current inside temperature.

        Args:
            energy_consumption (float): The energy consumed in kWh.
            inside_temperature (float): The current inside temperature in degrees Celsius.

        Returns:
            float: The heat power produced in kW.
        """
        return energy_consumption * self.efficiency_factor


class ElectricHeating(Heating):
    def __init__(self, electricity_carbon_cost: float = 0.233):
        super().__init__()
        self.electricity_carbon_cost = electricity_carbon_cost

    def carbon_costs(self, energy_consumption: float) -> float:
        """
        Calculate the carbon emissions based on the energy consumption.

        Args:
            energy_consumption (float): The amount of energy consumed in kWh.

        Returns:
            float: The carbon emissions in kg of CO2.
        """
        return energy_consumption * self.electricity_carbon_cost

    def compute_heat_power(self, energy_consumption: float, inside_temperature: float) -> float:
        """
        Calculate the heat power produced based on energy consumption and the current inside temperature.

        Args:
            energy_consumption (float): The energy consumed in kWh.
            inside_temperature (float): The current inside temperature in degrees Celsius.

        Returns:
            float: The heat power produced in kW.
        """
        # Power is directly the energy consumption in kW.
        return energy_consumption