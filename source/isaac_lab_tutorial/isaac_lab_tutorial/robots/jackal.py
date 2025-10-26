import isaaclab.sim as sim_utils
from isaaclab.assets import ArticulationCfg
from isaaclab.actuators import ImplicitActuatorCfg
from isaaclab.utils.assets import ISAAC_NUCLEUS_DIR

"""
Clearpath robot paths:
Robots/Clearpath/Dingo/dingo.usd
Robots/Clearpath/Dingo/dingo_basic.usd
Robots/Clearpath/Jackal/jackal.usd
Robots/Clearpath/RidgebackFranka/ridgeback_franka.usd
"""

JACKAL_CONFIG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(usd_path=f"{ISAAC_NUCLEUS_DIR}/Robots/Clearpath/Jackal/jackal.usd"),
    actuators={"wheel_acts": ImplicitActuatorCfg(joint_names_expr=[".*"], damping=None, stiffness=None)},
)
