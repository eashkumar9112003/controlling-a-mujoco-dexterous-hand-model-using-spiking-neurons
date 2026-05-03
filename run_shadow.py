import mujoco
import mujoco.viewer

model = mujoco.MjModel.from_xml_path(
"mujoco_menagerie/shadow_hand/scene_left.xml"
)

data = mujoco.MjData(model)

with mujoco.viewer.launch_passive(model, data):
    while True:
        mujoco.mj_step(model, data)
