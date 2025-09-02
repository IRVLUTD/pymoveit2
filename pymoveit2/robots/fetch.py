from typing import List

MOVE_GROUP_ARM: str = "arm_with_torso"
MOVE_GROUP_GRIPPER: str = "gripper"

OPEN_GRIPPER_JOINT_POSITIONS: List[float] = [0.05, 0.05]
CLOSED_GRIPPER_JOINT_POSITIONS: List[float] = [0.0, 0.0]


def joint_names() -> List[str]:
    return [
      "torso_lift_joint",
      "shoulder_pan_joint",
      "shoulder_lift_joint",
      "upperarm_roll_joint",
      "elbow_flex_joint",
      "forearm_roll_joint",
      "wrist_flex_joint",
      "wrist_roll_joint",  
    ]


def base_link_name() -> str:
    return "base_link"


def end_effector_name() -> str:
    return "wrist_roll_joint"


def gripper_joint_names() -> List[str]:
    return [
      "l_gripper_finger_joint",
      "r_gripper_finger_joint",
    ]
