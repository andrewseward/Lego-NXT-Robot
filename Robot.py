from time import sleep
from nxt.motor import Motor, PORT_B, PORT_C
from nxt.sensor.common import PORT_1, PORT_2, PORT_3, PORT_4
from nxt.sensor.generic import Touch, Sound, Light, Ultrasonic
from RobotMode import RobotMode



from nxt.locator import find_one_brick
FORTH = 100
BACK = -100
FREQ_C = 523
FREQ_D = 587
FREQ_E = 659

class Robot(object):
    r'''A high-level controller for the Alpha Rex model.

        This class implements methods for the most obvious actions performable
        by Alpha Rex, such as walk, wave its arms, and retrieve sensor samples.
        Additionally, it also allows direct access to the robot's components
        through public attributes.
    '''
    def __init__(self, brick='NXT'):
        r'''Creates a new Alpha Rex controller.

            brick
                Either an nxt.brick.Brick object, or an NXT brick's name as a
                string. If omitted, a Brick named 'NXT' is looked up.
        '''
        if isinstance(brick, basestring):
            brick = find_one_brick(name=brick)

        self.brick = brick
        self.leftMotor = Motor(brick, PORT_B)
        self.rightMotor = Motor(brick, PORT_C)
        self.motors = [self.leftMotor, self.rightMotor]

        self.touch = Touch(brick, PORT_3)
        #self.sound = Sound(brick, PORT_2)
        #self.light = Light(brick, PORT_3)
        self.ultrasonic = Ultrasonic(brick, PORT_4)

    def WarningNoise(self):
        self.brick.play_tone_and_wait(FREQ_E, 100)
        self.brick.play_tone_and_wait(FREQ_D, 100)
        self.brick.play_tone_and_wait(FREQ_C, 100)

    def OkNoise(self):
        self.brick.play_tone_and_wait(FREQ_C, 100)
        self.brick.play_tone_and_wait(FREQ_D, 100)
        self.brick.play_tone_and_wait(FREQ_E, 100)

    def StartWalk(self, power):
        for motor in self.motors:
            motor.run(power=power)

    def StopWalk(self):
        for motor in self.motors:
            motor.idle()

    def walk(self, secs, power=FORTH):
        self.StartWalk(power)
        sleep(secs)
        self.StopWalk()


    def IsButtonPressed(self):
        r'''Reads the Touch sensor's output.
        '''
        return self.touch.get_sample()

    def turn(self, direction, degrees):
        if (direction == RobotMode.Left):
            self.leftMotor.turn(-100, degrees)
            self.rightMotor.turn(100, degrees)
        else:
            self.rightMotor.turn(-100, degrees)
            self.leftMotor.turn(100, degrees)

    def getDistanceFromObstacle(self):
        return self.ultrasonic.get_sample()


