from dm_control import suite
from dm_control import viewer

# Load a Shadow Hand task
env = suite.load(domain_name="manipulator", task_name="bring_ball")

viewer.launch(env)
