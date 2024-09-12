import gymnasium as gym
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from src.office import Office

# Constants
TEMP_DIFF_FACTOR = 50000

class BasicEnv(gym.Env):
    """
    A basic gym environment for simulating temperature control in an office.
    """
    def __init__(self, start_year, start_month, start_day, start_hour, start_temperature, 
                end_year, end_month, end_day, end_hour, target_temperature, office) -> None:
        super().__init__()

        # Environment parameters
        self.state = datetime(start_year, start_month, start_day, start_hour)
        self.current_temperature = start_temperature
        self.target_temperature = target_temperature
        self.initial_time = self.state
        self.initial_temperature = start_temperature
        self.end_time = datetime(end_year, end_month, end_day, end_hour)
        self.office = office
        self.weather_condition = pd.read_csv('mannheim_weather_data_2024.csv')

        # Action space: Continuous power values from 0 to 10000
        self.action_space = gym.spaces.Box(low=np.array([0]), high=np.array([10000]), dtype=np.float32)

        # Observation space: [current_temperature, hour_of_day]
        self.observation_space = gym.spaces.Box(low=np.array([-50]), high=np.array([50]), dtype=np.float32)

        # Additional tracking variables
        self.done = False
        self.reward = 0
        self.current_emissions = 0

    def step(self, heat_power):
        """
        Advance the environment by one time step, given the action (heat_power).
        """
        reward = 0
        self.state += timedelta(hours=1)
        current_weather = self.get_current_weather(self.state)
        self.current_temperature = self.office.compute_next_temperature(self.current_temperature, current_weather, heat_power)

        # Calculate reward
        reward -= heat_power
        if self.state >= self.end_time:
            self.done = True
            reward -= 100 * abs(self.current_temperature - self.target_temperature)  # Penalize temperature difference
        self.reward += float(reward)

        hour_of_day = self.state.hour
        observation = self.current_temperature

        # Optional info
        info = {}

        return observation, float(reward), self.done, False, info


    def reset(self, seed=None, return_info=False, options=None):
        self.state = self.initial_time
        self.current_temperature = self.initial_temperature
        self.done = False
        self.reward = 0
        self.current_emissions = 0

        # Initialize random seed if provided
        if seed is not None:
            np.random.seed(seed)

        # Initial observation
        hour_of_day = self.state.hour
        observation = np.array([self.current_temperature], dtype=np.float32)  # Ensure dtype is float32

        info = {}  # Return an empty info dictionary

        return observation, info

    def render(self, mode='human'):
        """
        Print the current state and information for human interpretation.
        """
        print(f'Time: {self.state}, Temperature: {self.current_temperature}, Target: {self.target_temperature}')
        print(f'Time left: {self.end_time - self.state}')

    def get_current_weather(self, time: datetime) -> float:
        """
        Get the weather temperature for a specific time.
        """
        try:
            year, month, day, hour = time.year, time.month, time.day, time.hour
            temperature = self.weather_condition.loc[
                (self.weather_condition['year'] == year) &
                (self.weather_condition['month'] == month) &
                (self.weather_condition['day'] == day) &
                (self.weather_condition['hour'] == hour), 
                'temperature'
            ].values[0]
            return temperature
        except IndexError:
            raise ValueError(f"No weather data available for {time}. Ensure the dataset includes this timestamp.")
