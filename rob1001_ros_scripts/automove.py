import time
import random

# Mock functions to simulate robot movement and sensor readings
def move_forward():
    print("Moving forward")

def turn_left():
    print("Turning left")
def turn_right():
    print("Turning right")

def check_front_sensor():
    # Simulate obstacle detection: True means an obstacle is detected
    return random.choice([True, False])

def check_left_sensor():
    # Simulate obstacle detection
    return random.choice([True, False])

def check_right_sensor():
    # Simulate obstacle detection
    return random.choice([True, False])

# Main navigation function
def navigate_room():
    while True:
        if not check_front_sensor():
            move_forward()
        else:
            if not check_left_sensor():
                turn_left()
            elif not check_right_sensor():
                turn_right()
            else:
                # If obstacles are all around, turn around (not implemented)
                turn_left()
                turn_left()

        time.sleep(1)  # Pause for a bit before checking sensors again

# Start the navigation
navigate_room()