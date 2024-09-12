from src.heating import GasHeating
from src.office import Office
from stable_baselines3 import PPO
from stable_baselines3.common.env_checker import check_env
from stable_baselines3.common.env_util import make_vec_env
from src.environment import BasicEnv
from stable_baselines3.common.vec_env import DummyVecEnv


heating = GasHeating()

office = Office(
    heating=heating,
    volume=16242,
    wall_area=510,
    window_area=100,
    roof_area=1800,
    u_wall=0.4,
    u_window=2,
    u_roof=0.3
)

start_year = 2022
start_month = 10
start_day = 12
start_hour = 19
start_temperature = 22

end_year = 2022
end_month = 10
end_day = 13
end_hour = 6
target_temperature = 22

# Wrap the environment
env = DummyVecEnv([lambda: BasicEnv(start_year, start_month, start_day, start_hour, start_temperature, end_year, end_month, end_day, end_hour, target_temperature, office)])

# Train the model
model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=10000)

# Evaluate the model
obs = env.reset()  # Note: reset() returns only observation
done = False
actions = []
while not done:
    action, _states = model.predict(obs)
    actions.append(action)
    obs, rewards, done, info = env.step(action)  # Ensure your step method matches this
    env.render()

print(actions)