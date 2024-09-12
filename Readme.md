# Office Heating Optimization for Decarbonization

## Overview

This project aims to help Roche reduce their CO2 carbon footprint by optimizing the office heating system. Our approach involves modeling the office environment, evaluating different heating methods, and leveraging reinforcement learning to suggest the most efficient heating plan. By considering target temperatures, weather forecasts, and office occupancy, we aim to provide actionable insights for reducing energy consumption and carbon emissions.

## Project Structure

The project is organized into the following main components:

1. **Office Model (`src/office.py`)**
   - **`Office` Class**: Models the office environment including volume, wall area, window area, roof area, and heat loss coefficients. Computes the heat loss and next temperature based on heating power and occupancy.
   
2. **Heating Systems (`src/heating.py`)**
   - **`Heating` Class**: Abstract base class for different heating systems.
   - **`GasHeating` Class**: Implements gas heating with efficiency and carbon emission calculations.
   - **`PumpHeating` Class**: Implements pump heating with a higher efficiency factor and associated carbon costs.
   - **`ElectricHeating` Class**: Implements electric heating with direct energy consumption and carbon emission calculations.
   
3. **Reinforcement Learning Environment (`src/env.py`)**
   - **`BasicEnv` Class**: A Gym environment simulating temperature control in an office. Includes action and observation spaces, as well as reward mechanisms based on heating power and temperature differences.

## Usage

### Setting Up

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/office-heating-optimization.git
   cd office-heating-optimization
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure you have the weather data CSV file (`mannheim_weather_data_2024.csv`) in the `src` directory.

### Running the Simulation

To run a simulation, you can use the provided Gym environment. Here's a basic example:

```python
from src.office import Office
from src.heating import GasHeating, PumpHeating, ElectricHeating
from src.env import BasicEnv

# Initialize heating systems
gas_heating = GasHeating()
pump_heating = PumpHeating()
electric_heating = ElectricHeating()

# Create an office model
office = Office(
    heating=gas_heating,
    volume=1000,
    wall_area=200,
    window_area=50,
    roof_area=100,
    u_wall=0.3,
    u_window=0.6,
    u_roof=0.4
)

# Initialize the environment
env = BasicEnv(
    start_year=2024, start_month=1, start_day=1, start_hour=0,
    start_temperature=20, end_year=2024, end_month=1, end_day=2, end_hour=0,
    target_temperature=21, office=office
)

# Run a sample step
action = 5000  # Example heating power
observation, reward, done, _, _ = env.step(action)
print(f"Observation: {observation}, Reward: {reward}, Done: {done}")
```

## Next Steps

1. **Integration**: Connect the implementation with existing heating systems at Roche.
2. **Recommendations**: Develop and provide recommendations for office occupancy to optimize heating.
3. **API Development**: Implement an API to facilitate the use of the optimization model for ease of integration and deployment.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have suggestions or improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.