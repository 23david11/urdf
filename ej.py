import pybullet as p
import pybullet_data
import time
import math

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.8)

planeID = p.loadURDF("plane.urdf")

euler_angles = [0, 0, math.pi]
startOrientation = p.getQuaternionFromEuler(euler_angles)
start_position = [0, 0, 1]

robotID = p.loadURDF("ej.urdf", start_position, startOrientation)

frictionID = p.addUserDebugParameter("friction", 0, 10, 5)
torqueID = p.addUserDebugParameter("torque", -10, 10, 0)

for i in range (100000):

    friction = p.readUserDebugParameter(frictionID)
    torque = p.readUserDebugParameter(torqueID)

    p.setJointMotorControl2(robotID, 1, p.TORQUE_CONTROL, force=torque)
    p.setJointMotorControl2(robotID, 1, p.VELOCITY_CONTROL,
                            targetVelocity=0, force=friction)


    p.stepSimulation()
    time.sleep(1./240.)

p.disconnect()