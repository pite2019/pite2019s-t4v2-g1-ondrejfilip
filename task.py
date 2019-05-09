from random import gauss
import logging
import time


class Plane:

    def __init__(self):
        self.tilt = 0

    def tilt_correction(self):
        if self.tilt > 0:
            self.tilt -= 2
        else:
            self.tilt += 2

    def __str__(self):
        return "The tilt is {}°".format(self.tilt)

class Environment:

    def __init__(self, plane):
        self.plane = plane
        self.turbulence = 0

    def flight_simulation(self):
        self.turbulence = gauss(mu=0, sigma=3)
        self.plane.tilt += self.turbulence
        self.plane.tilt_correction()

def main():
    logging.basicConfig(level=logging.DEBUG)
    plane1 = Plane()
    environment1 = Environment(plane1)

    while True:
        environment1.flight_simulation()
        logging.debug('New turbulence: {}, Tilt after correction: {}'
                      .format(environment1.turbulence, plane1.tilt))
        time.sleep(4)

if __name__ == '__main__':
    main()
