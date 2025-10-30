# SPDX-FileCopyrightText: Copyright (c) 2025 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# All rights reserved.
#
# SPDX-License-Identifier: Apache-2.0

from isaac_lab_tutorial.robots.jackal import JACKAL_CONFIG
import isaaclab.sim as sim_utils
from isaaclab.assets import ArticulationCfg
from isaaclab.envs import DirectRLEnvCfg
from isaaclab.scene import InteractiveSceneCfg
from isaaclab.sim import SimulationCfg
from isaaclab.utils import configclass
from isaaclab.sensors import CameraCfg, TiledCameraCfg, RayCasterCfg, patterns

@configclass
class JackalDriveEnvCfg(DirectRLEnvCfg):
    # env
    decimation = 2
    episode_length_s = 5.0
    # - spaces definition
    action_space = 2
    # observation_space = 9
    observation_space = 3
    state_space = 0
    # simulation
    sim: SimulationCfg = SimulationCfg(dt=1 / 120, render_interval=decimation)
    # robot(s)
    robot_cfg: ArticulationCfg = JACKAL_CONFIG.replace(prim_path="/World/envs/env_.*/Robot")

    tiled_camera: TiledCameraCfg = TiledCameraCfg(
        prim_path="/World/envs/env_.*/Robot/base_link/bumblebee_stereo_camera_frame/"
                  "bumblebee_stereo_left_frame/bumblebee_stereo_left_camera",
        offset=CameraCfg.OffsetCfg(pos=(0.0, 0.0, 0.0), rot=(-0.5, -0.5, 0.5, 0.5), convention="ros"),
        data_types=["rgb"],
        spawn=None,
        width=640,
        height=480,
    )
    ray_caster = RayCasterCfg(
        prim_path="/World/envs/env_.*/Robot/base_link/sick_lms1xx_lidar_frame/Lidar",
        update_period=1 / 60,
        offset=RayCasterCfg.OffsetCfg(pos=(0.12, 0, 0.333)),
        mesh_prim_paths=["/World/ground"],
        ray_alignment="yaw",
        pattern_cfg=patterns.LidarPatternCfg(
            channels=100, vertical_fov_range=[-90, 90], horizontal_fov_range=[-90, 90], horizontal_res=1.0
        ),
            debug_vis=True,
    )
    # camera = CameraCfg(
    #     prim_path="{ENV_REGEX_NS}/Robot/base_link/bumblebee_stereo_camera_frame/"
    #               "bumblebee_stereo_left_frame/bumblebee_stereo_left_camera",
    #     update_period=0.1,
    #     height=480,
    #     width=640,
    #     data_types=["rgb", "distance_to_image_plane"],
    #     spawn=sim_utils.PinholeCameraCfg(
    #         focal_length=24.0, focus_distance=400.0, horizontal_aperture=20.955, clipping_range=(0.1, 1.0e5)
    #     ),
    #     offset=CameraCfg.OffsetCfg(pos=(0.0, 0.06, 0.0), rot=(-0.5, -0.5, 0.5, 0.5), convention="ros"),
    # )


    # scene
    scene: InteractiveSceneCfg = InteractiveSceneCfg(num_envs=2, env_spacing=4.0, replicate_physics=True)
    # jackal: ['front_left_wheel_joint', 'front_right_wheel_joint', 'rear_left_wheel_joint', 'rear_right_wheel_joint']
    # jackal_basic: ['front_left_wheel', 'front_right_wheel', 'rear_left_wheel', 'rear_right_wheel']
    # dof_names = ["left_wheel_joint", "right_wheel_joint"]
    # dof_names = ['front_left_wheel', 'front_right_wheel']
    dof_names = ['front_left_wheel_joint', 'front_right_wheel_joint']
    # camera