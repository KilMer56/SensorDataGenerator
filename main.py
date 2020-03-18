import argparse, random
import json

from datetime import datetime, timedelta
from time import sleep, time

class Sensor(object):
    """
    Class that represents a sensor that will mock values
    """

    def __init__(self, min, max, step, label):
        self.min = min
        self.max = max
        self.step = step
        self.label = label
        self.value = round(random.uniform(self.min, self.max), 2)

    def next(self):
        """
        Get the next message to send by updating the date and the value

        :return message : The next message to send
        """

        # Get the new date
        curr_date = datetime.now()
        val = 0

        # Create the next message
        message = {"date": curr_date.strftime("%Y-%m-%d %H:%M:%S"), "label": self.label, "value": self.value}

        # Update the value with a random step in the range specified
        while val == 0 or val < self.min or val > self.max:
            val = round(float(self.value + random.uniform(-self.step, self.step)), 2)
        
        self.value = val
        
        return message

class SensorGenerator(object):
    """
    Class that represents a generator that contains a list of sensors.
    """

    def __init__(self):
        self.sensors = []
        self.rate = 5
        
    def parseFile(self):
        """
        Parse the 'config.json' file which contains informations about the sensors to generate
        """

        print("[*] Open the config.json file ...")

        # Read the file and create the list of sensors
        with open('config.json') as json_file:
            data = json.load(json_file)
            self.rate = int(data['rate'])

            for sensorData in data['sensors']:
                self.createSensor(sensorData)
    
    def createSensor(self, values):
        """
        Create a sensor from the values in parameters and add it to the list.

        :param values : Properties of the sensor
        :type values : dict
        """

        # Parse the params
        min_val = float(values['min'])
        max_val = float(values['max'])
        step = float(values['step']) if values['step'] else float(5)
        label = str(values['label']) if values['label'] else "Unknown Sensor"

        # Create the sensor
        print ("[*] Creating '"+label+"' Sensor -> Min: "+str(min_val)+", Max: "+str(max_val)+", Step: "+str(step))
        sensor = Sensor(min_val, max_val, step, label)

        self.sensors.append(sensor)

    def run(self):
        """
        Run the generator.
        """

        try:
            # Infinite Loop that sends informations every 'rate' seconds
            while True:
                sleep(self.rate)

                for sensor in self.sensors:
                    message = sensor.next()
                    print ("[*] Sending data : "+str(message))
        except KeyboardInterrupt:
            pass

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Sensor data generator for spark book")
    
    # List of arguments
    parser.add_argument("--file", "-f",
                        nargs="?",
                        const=True,
                        default=False,
                        help="Need to read the conf from the json file")
    parser.add_argument("--min", "-min",
                        nargs="?",
                        help="Minimum value of the sensor")
    parser.add_argument("--max", "-max",
                        nargs="?",
                        help="Maximum value of the sensor")
    parser.add_argument("--rate", "-r",
                        nargs="?",
                        help="Number of seconds between two messages")
    parser.add_argument("--step", "-s",
                        nargs="?",
                        help="Step delta between every value")
    parser.add_argument("--label", "-l",
                        nargs="?",
                        help="Label of the sensor")
    parser.add_argument("--value", "-v",
                        nargs="?",
                        help="First value of the sensor")

    # Parse the arguments
    args = parser.parse_args()

    # Create the sensor generator
    generator = SensorGenerator()

    # Parse the life if needed or parse the arguments
    if args.file:
        generator.parseFile()
    else:
        if args.rate:
            generator.rate = int(args.rate)
        
        generator.createSensor(vars(args))

    # Run the generator
    generator.run()

        