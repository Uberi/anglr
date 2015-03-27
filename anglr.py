#!/usr/bin/env python3

"""Planar angle mathematics library for Python."""

__author__ = "Anthony Zhang (Uberi)"
__version__ = "1.0.2"
__license__ = "BSD"

import math, numbers

TAU = math.pi * 2

class Angle:
    def __init__(self, value = 0, mode = "radians"):
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
    def degrees(self): return math.degrees(self.radians)
    @degrees.setter
    def degrees(self, value): self.radians = math.radians(value)
    @property
    def gradians(self): return self.radians * 400 / TAU
    @gradians.setter
    def gradians(self, value): self.radians = value * TAU / 400
    @property
    def hours(self): return self.radians * 24 / TAU
    @hours.setter
    def hours(self, value): self.radians = value * TAU / 24
    @property
    def arcminutes(self): return (self.radians * 360 / TAU) * 60
    @arcminutes.setter
    def arcminutes(self, value): self.radians = (value / 60) * TAU / 360
    @property
    def arcseconds(self): return (self.radians * 360 / TAU) * 3600
    @arcseconds.setter
    def arcseconds(self, value): self.radians = (value / 3600) * TAU / 360
    @property
    def vector(self): return math.cos(self.radians), math.sin(self.radians)
    @vector.setter
    def vector(self, value):
        if len(value) != 2: raise ValueError("Invalid vector \"{}\"".format(value))
        if value[0] == 0 == value[1]: raise ValueError("Zero vector (0, 0) has undefined angle".format(value))
        self.radians = math.atan2(value[1], value[0])
    @property
    def x(self): return math.cos(self.radians)
    @property
    def y(self): return math.sin(self.radians)
    
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
    def dump(self): return "<Angle: {} radians, {} degrees, {} gradians, {} hours, {} arcminutes, {} arcseconds, offset ({}, {})>".format(self.radians, self.degrees, self.gradians, self.hours, self.arcminutes, self.arcseconds, self.x, self.y)
    
    # circle functions
    def normalized(self, lower = 0, upper = None):
        if upper is None: upper = lower + TAU
        if lower > upper: lower, upper = upper, lower # swap bounds if upper bound is greater than lower bound
        return Angle(lower + (self.radians % TAU) * (upper - lower))
    def angle_between_clockwise(self, angle):
        return Angle((Angle(angle).radians - self.radians) % TAU)
    def angle_between(self, angle):
        angle = Angle(angle)
        return min(self.angle_between_clockwise(angle), angle.angle_between_clockwise(self))
    def angle_within(self, lower, upper, strictly_within = False):
        if lower > upper: lower, upper = upper, lower # swap bounds if upper bound is greater than lower bound
        lower, upper = Angle(lower), Angle(upper)
        
        # transform all angles into a coordinate space where the lower angle is the positive X-axis to make comparison easier
        value = (self.radians - lower.radians) % TAU
        upper_bound = (upper.radians - lower.radians) % TAU
        if strictly_within: return 0 < value < upper_bound
        return 0 <= value <= upper_bound

if __name__ == "__main__":
    from math import pi

    assert str(Angle()) == "0 rad"
    assert str(Angle(87 * pi / 2)) == "136.659280431156 rad"
    assert str(Angle(pi / 2, "radians")) == "1.5707963267948966 rad"
    assert str(Angle(Angle(pi / 2, "radians"))) == "1.5707963267948966 rad" # same as above
    assert str(Angle(64.2, "degrees")) == "1.1205013797803596 rad"
    assert str(Angle(384.9, "gradians")) == "6.0459950618335565 rad"
    assert str(Angle(4.5, "hours")) == "1.1780972450961724 rad"
    assert str(Angle(203.8, "arcminutes")) == "0.059283016926074066 rad"
    assert str(Angle(42352.7, "arcseconds")) == "0.2053316839192784 rad"
    assert str(Angle((56, 32), "vector")) == "0.5191461142465229 rad" # angle in standard position - counterclockwise from positive X-axis

    x = Angle(58.3)
    assert "{} {} {} {} {} {} {} {} {} {} {}".format([x], str(x), x.radians, x.degrees, x.gradians, x.hours, x.arcminutes, x.arcseconds, x.vector, x.x, x.y) == "[<Angle 58.3 rad>] 58.3 rad 58.3 3340.3439456126994 3711.4932729029993 222.68959637417993 200420.63673676195 12025238.204205718 (-0.17955679797714189, 0.9837476080276871) -0.17955679797714189 0.9837476080276871"
    assert str(complex(x)) == "(58.3+0j)"
    assert str(float(x)) == "58.3"
    assert str(int(x)) == "58"
    x.radians = pi / 2
    assert str(x.dump()) == "<Angle: 1.5707963267948966 radians, 90.0 degrees, 100.0 gradians, 6.0 hours, 5400.0 arcminutes, 324000.0 arcseconds, offset (6.123233995736766e-17, 1.0)>"
    x.degrees = 64.2
    assert str(x.dump()) == "<Angle: 1.1205013797803596 radians, 64.2 degrees, 71.33333333333334 gradians, 4.28 hours, 3852.0 arcminutes, 231120.0 arcseconds, offset (0.4352310993723275, 0.9003187714021935)>"
    x.gradians = 384.9
    assert str(x.dump()) == "<Angle: 6.0459950618335565 radians, 346.40999999999997 degrees, 384.9 gradians, 23.093999999999998 hours, 20784.6 arcminutes, 1247076.0 arcseconds, offset (0.9720020258153625, -0.23497247032542193)>"
    x.hours = 4.5
    assert str(x.dump()) == "<Angle: 1.1780972450961724 radians, 67.5 degrees, 75.0 gradians, 4.5 hours, 4050.0 arcminutes, 243000.0 arcseconds, offset (0.38268343236508984, 0.9238795325112867)>"
    x.arcminutes = 203.8
    assert str(x.dump()) == "<Angle: 0.059283016926074066 radians, 3.396666666666667 degrees, 3.7740740740740746 gradians, 0.22644444444444445 hours, 203.8 arcminutes, 12228.000000000002 arcseconds, offset (0.9982432765393775, 0.05924829823655638)>"
    x.arcseconds = 42352.7
    assert str(x.dump()) == "<Angle: 0.2053316839192784 radians, 11.764638888888886 degrees, 13.071820987654316 gradians, 0.7843092592592591 hours, 705.8783333333331 arcminutes, 42352.69999999999 arcseconds, offset (0.9789934107119936, 0.20389188748574036)>"
    x.vector = (56, 32)
    assert str(x.dump()) == "<Angle: 0.5191461142465229 radians, 29.74488129694222 degrees, 33.04986810771358 gradians, 1.9829920864628148 hours, 1784.6928778165334 arcminutes, 107081.57266899201 arcseconds, offset (0.8682431421244592, 0.49613893835683376)>"

    assert str(Angle(pi / 6) + Angle(2 * pi / 3)) == "2.617993877991494 rad"
    assert str(x * 2 + Angle(3 * pi / 4) / 4 + 5 * Angle(pi / 3)) == "6.86332860702412 rad"
    assert str(-abs(+Angle(pi))) == "-3.141592653589793 rad"
    assert str(round(Angle(-75.87))) == "-76 rad"
    assert str(Angle(-4.3) <= Angle(pi / 4) > Angle(0.118) == Angle(0.118)) == "True"
    assert str(Angle(-870.3, "gradians").normalized()) == "32.540085710391615 rad"
    assert str(Angle(-870.3, "gradians").normalized(0)) == "32.540085710391615 rad" # same as above
    assert str(Angle(-870.3, "gradians").normalized(0, 2 * pi)) == "32.540085710391615 rad" # same as above
    assert str(Angle(-870.3, "gradians").normalized(-pi, pi)) == "29.398493056801822 rad"
    assert str(Angle(-870.3, "gradians").normalized(-pi, 0)) == "13.128450201606015 rad"
    assert str(Angle(1, "degrees").angle_between_clockwise(Angle(0, "degrees"))) == "6.265732014659643 rad"
    assert str(Angle(1, "degrees").angle_between(Angle(0, "degrees"))) == "0.017453292519943295 rad"
    assert str(Angle(0, "degrees").angle_within(Angle(-45, "degrees"), Angle(45, "degrees"))) == "True"
    assert str(Angle(-1, "degrees").angle_within(Angle(-1, "degrees"), Angle(1, "degrees"), strictly_within=True)) == "False"
    
    print("All tests passed!")
