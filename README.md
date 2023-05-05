# Financial Interpolation Library
The Financial Interpolation Library is a Python library for interpolating financial data, such as interest rates and financial values, using various interpolation methods, including linear interpolation, cubic spline, and exponential interpolation.

This library is especially useful for financial analysts, financial software developers, and researchers working with financial data who need to perform interpolations in a simple and efficient manner.

## Installation
Install the library using pip:
```pip install financial-interpolation```

## Dependencies
This library depends on the scipy package.

## Usage
Import the desired interpolation class and create an instance:
``` 
from interpolations import LinearInterpolator, CubicSplineInterpolator, ExponentialInterpolator
    
linear_interpolator = LinearInterpolator()
cubic_spline_interpolator = CubicSplineInterpolator()
exponential_interpolator = ExponentialInterpolator()
```
Use the instance to perform the interpolation, passing in the required arguments:
```
# Example of linear interpolation
y0 = 1
y1 = 2
WD0 = 0
WD1 = 252
WD = 126
result = linear_interpolator.interpolate(y0, y1, WD0, WD1, WD)
    
# Example of cubic spline interpolation
x_values = [0, 1, 2, 3]
y_values = [0, 2, 3, 1]
x = 1.5
result = cubic_spline_interpolator.interpolate(x_values, y_values, x)
    
# Example of exponential interpolation
y0 = 0.02
y1 = 0.03
WD0 = 0
WD1 = 252
WD = 126
WD_prime = 252
result = exponential_interpolator.interpolate(y0, y1, WD0, WD1, WD, WD_prime)
```
## Documentation
For more information on the available classes and methods, please refer to the full documentation on the documentation page.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contributions
Contributions are welcome! Please open an Issue to report bugs or propose improvements, and use a Pull Request to submit your changes.
