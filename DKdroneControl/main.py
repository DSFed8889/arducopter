from dronekit import connect
import time

# Connect to the Vehicle (in this case a UDP endpoint)
vehicle = connect('COM34', wait_ready=True, baud=57600)

print("Autopilot Firmware version: %s" % vehicle.version)
# print("Auilot capabilities (supports ftp): %s" % vehicle.capabilities.ftp)
print("Global Location: %s" % vehicle.location.global_frame)
print("Global Location (relative altitude): %s" % vehicle.location.global_relative_frame)
print("Local Location: %s" % vehicle.location.local_frame)    #NED
while True:
    print("%s" % vehicle.attitude)
    print("Velocity: %s" % vehicle.velocity)
    print("Armed: %s" % vehicle.armed)    # settable
    time.sleep(1)
