from src.heating import GasHeating, PumpHeating, ElectricHeating
from src.Office import Office

heating = GasHeating()

office1 = Office(
    heating=heating,
    volume=16242,
    wall_area=510,
    window_area=100,
    roof_area=1800,
    u_wall=0.4,
    u_window=2,
    u_roof=0.3
)

heating2 = PumpHeating()
office2 = Office(
    heating=heating2,
    volume=16242,
    wall_area=510,
    window_area=100,
    roof_area=1800,
    u_wall=0.4,
    u_window=2,
    u_roof=0.3
)

heating3 = ElectricHeating()
office3 = Office(
    heating=heating3,
    volume=16242,
    wall_area=510,
    window_area=100,
    roof_area=1800,
    u_wall=0.4,
    u_window=2,
    u_roof=0.3
)
temperature = office1.compute_next_temperature(24, -5, 30)
print(temperature)

temperature = office2.compute_next_temperature(24, -5, 30)
print(temperature)

temperature = office3.compute_next_temperature(24, -5, 30)
print(temperature)