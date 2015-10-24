#!/usr/bin/env python3

"""Planar angle mathematics library for Python."""

__author__ = "Anthony Zhang (Uberi)"
__version__ = "1.1.0"
__license__ = "BSD"

import math, numbers

TAU = math.pi * 2

class Angle:
    def __init__(self, value = 0, mode = "radians"):
        """
        Creates an `Angle` instance representing the angle `value` in the angular unit specified by `mode`.
        
        `mode` can be "radians", "degrees", "gradians", "hours", "arcminutes", "arcseconds", or "vector" (see `angle_instance.vector` for more info).
        """
        if isinstance(value, Angle): self.radians = value.radians
        elif mode == "vector": self.vector = value
        elif not isinstance(value, numbers.Real): raise ValueError("Value \"{}\" must be a real-number-like object".format(value))
        elif mode == "radians": self.radians = value
        elif mode == "degrees": self.degrees = value
        elif mode == "gradians": self.gradians = value
        elif mode == "hours": self.hours = value
        elif mode == "arcminutes": self.arcminutes = value
        elif mode == "arcseconds": self.arcseconds = value
        else: raise ValueError("Angle mode \"{}\" must be one of \"radians\", \"degrees\", \"gradians\", \"hours\", \"arcminutes\", \"arcseconds\", or \"vector\"".format(mode))
    
    # various conversions between angles and numerical representations of angles
    @property
    def degrees(self):
        """Returns the represented angle in degrees as a plain number."""
        return math.degrees(self.radians)
    @degrees.setter
    def degrees(self, value):
        """Sets the represented angle to the angle represented by `value` in degrees."""
        self.radians = math.radians(value)
    @property
    def gradians(self):
        """Returns the represented angle in gradians as a plain number."""
        return self.radians * 400 / TAU
    @gradians.setter
    def gradians(self, value):
        """Sets the represented angle to the angle represented by `value` in gradians."""
        self.radians = value * TAU / 400
    @property
    def hours(self):
        """Returns the represented angle in hours as a plain number."""
        return self.radians * 24 / TAU
    @hours.setter
    def hours(self, value):
        """Sets the represented angle to the angle represented by `value` in hours."""
        self.radians = value * TAU / 24
    @property
    def arcminutes(self):
        """Returns the represented angle in arcminutes as a plain number."""
        return (self.radians * 360 / TAU) * 60
    @arcminutes.setter
    def arcminutes(self, value):
        """Sets the represented angle to the angle represented by `value` in arcminutes."""
        self.radians = (value / 60) * TAU / 360
    @property
    def arcseconds(self):
        """Returns the represented angle in arcseconds as a plain number."""
        return (self.radians * 360 / TAU) * 3600
    @arcseconds.setter
    def arcseconds(self, value):
        """Sets the represented angle to the angle represented by `value` in arcseconds."""
        self.radians = (value / 3600) * TAU / 360
    @property
    def vector(self):
        """Returns a 2D unit vector `(X_VALUE, Y_VALUE)` that is at the represented angle counterclockwise from the positive X axis (standard position)."""
        return math.cos(self.radians), math.sin(self.radians)
    @vector.setter
    def vector(self, value):
        """Sets the represented angle to the angle that `value`, a vector `(X_VALUE, Y_VALUE)`, has counterclockwise from the positive X axis (standard position)."""
        if len(value) != 2: raise ValueError("Invalid vector \"{}\"".format(value))
        if value[0] == 0 == value[1]: raise ValueError("Zero vector (0, 0) has undefined angle".format(value))
        self.radians = math.atan2(value[1], value[0])
    @property
    def x(self):
        """Returns the X axis component of a 2D unit vector `(X_VALUE, Y_VALUE)` at the represented angle counterclockwise from the positive X axis (standard position)."""
        return math.cos(self.radians)
    @property
    def y(self):
        """Returns the Y axis component of a 2D unit vector `(X_VALUE, Y_VALUE)` at the represented angle counterclockwise from the positive X axis (standard position)."""
        return math.sin(self.radians)
    
    # make it behave like a real number
    def __add__(self, angle):
        if not isinstance(angle, Angle): raise ValueError("Addend \"{}\" must be an angle".format(angle))
        return Angle(self.radians + angle.radians)
    def __sub__(self, angle):
        if not isinstance(angle, Angle): raise ValueError("Subtrahend \"{}\" must be an angle".format(angle))
        return Angle(self.radians - angle.radians)
    def __mul__(self, value):
        if not isinstance(value, numbers.Real): raise ValueError("Multiplicand \"{}\" must be numerical".format(value))
        return Angle(self.radians * value)
    def __truediv__(self, value):
        if not isinstance(value, numbers.Real): raise ValueError("Divisor \"{}\" must be numerical".format(value))
        return Angle(self.radians / value)
    def __rmul__(self, value):
        if not isinstance(value, numbers.Real): raise ValueError("Multiplicand \"{}\" must be numerical".format(value))
        return Angle(value * self.radians)
    def __neg__(self): return Angle(-self.radians)
    def __pos__(self): return Angle(self.radians)
    def __abs__(self): return Angle(abs(self.radians))
    def __round__(self): return Angle(round(self.radians))
    def __lt__(self, angle):
        if isinstance(angle, Angle): return self.radians < angle.radians
        return NotImplemented
    def __le__(self, angle):
        if isinstance(angle, Angle): return self.radians <= angle.radians
        return NotImplemented
    def __eq__(self, angle):
        if isinstance(angle, Angle): return self.radians == angle.radians
        return NotImplemented
    
    # type conversions
    def __complex__(self): return complex(self.radians)
    def __int__(self): return int(self.radians)
    def __float__(self): return float(self.radians)
    def __str__(self): return "{} rad".format(self.radians)
    def __repr__(self): return "<Angle {} rad>".format(self.radians)
    def __hash__(self): return hash(self.radians)
    def dump(self):
        """Returns a string representation of the `Angle` instance that contains the represented angle in various units and formats, useful for debugging purposes."""
        return "<Angle: {} radians, {} degrees, {} gradians, {} hours, {} arcminutes, {} arcseconds, offset ({}, {})>".format(self.radians, self.degrees, self.gradians, self.hours, self.arcminutes, self.arcseconds, self.x, self.y)
    
    # unit circle functions
    def normalized(self, lower = 0, upper = None):
        """Returns a new `Angle` instance that represents the angle normalized on the unit circle to be between `lower` (inclusive) and `upper` (exclusive, defaults to `lower + TAU`)."""
        if upper is None: upper = lower + TAU
        if lower > upper: lower, upper = upper, lower # swap bounds if upper bound is greater than lower bound
        return Angle(lower + (self.radians % TAU) * (upper - lower))
    def angle_between_clockwise(self, angle):
        """Returns a new `Angle` instance that represents the clockwise angle from this `Angle` instance to `angle` on the unit circle (this is always non-negative)."""
        return Angle((Angle(angle).radians - self.radians) % TAU)
    def angle_between(self, angle):
        """Returns a new `Angle` instance that represents the smallest of the two possible angles between `Angle` instance to `angle` on the unit circle (this is always non-negative)."""
        angle = Angle(angle)
        return min(self.angle_between_clockwise(angle), angle.angle_between_clockwise(self))
    def angle_within(self, lower, upper, strictly_within = False):
        """Returns `True` if this `Angle` instance is within the angles `lower` and `upper` on the unit circle - inclusive if `strictly_within` is falsy, exclusive otherwise. Returns `False` otherwise."""
        if lower > upper: lower, upper = upper, lower # swap bounds if upper bound is greater than lower bound
        lower, upper = Angle(lower), Angle(upper)
        
        # transform all angles into a coordinate space where the lower angle is the positive X-axis to make comparison easier
        value = (self.radians - lower.radians) % TAU
        upper_bound = (upper.radians - lower.radians) % TAU
        if strictly_within: return 0 < value < upper_bound
        return 0 <= value <= upper_bound
    def angle_to(self, angle):
        """Returns a new `Angle` instance that represents the angle with the smallest magnitude that, when added to this `Angle` instance, results in `angle` on the unit circle."""
        clockwise = self.angle_between_clockwise(angle)
        counterclockwise = -angle.angle_between_clockwise(self)
        return clockwise if clockwise <= abs(counterclockwise) else counterclockwise
