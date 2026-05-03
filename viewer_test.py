import mujoco
import mujoco.viewer

model = mujoco.MjModel.from_xml_string("""
<mujoco>
  <worldbody>
    <geom type="plane" size="5 5 0.1"/>
    <body pos="0 0 1">
      <geom type="sphere" size="0.1"/>
    </body>
  </worldbody>
</mujoco>
""")

data = mujoco.MjData(model)

with mujoco.viewer.launch_passive(model, data):
    while True:
        mujoco.mj_step(model, data)
