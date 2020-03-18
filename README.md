# Sensor Data Generator

A very simple and easy to use data generator in order to mock Sensors.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Support](#support)
- [Contributing](#contributing)

## Installation

To install the project, you juste need to run :

```sh
git clone https://github.com/KilMer56/SensorDataGenerator.git
python3 main.py [params]
```

## Parameters

| Parameter | Short | Type    | Description                               | Default   |
| --------- | :---: | :-----: | :---------------------------------------: | --------: |
| --file    |  -f   | Boolean |  If the config is in the config.json file | False     |
| --min     |  -min | Float   |  Minimum value of the sensor              | None      |
| --max     |  -max | Float   |       Maximum value of the sensor         | None      |
| --rate    |  -r   | Integer | Number of seconds between two messages    | 5         |
| --step    |  -s   | Float   |  Step delta between every value           | None      |
| --label   |  -l   | String  |  Label of the sensor                      | 'Unknown' |
| --value   |  -v   | String  |  First value of the sensor                | Random    |


Feel free to suggest any parameter you want to add.

## Support

Please [open an issue](https://github.com/KilMer56/SensorDataGenerator/issues/new) for support.

## Contributing

Please contribute using [Github Flow](https://guides.github.com/introduction/flow/). Create a branch, add commits, and [open a pull request](https://github.com/KilMer56/SensorDataGenerator/compare/).