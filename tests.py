import unittest
from math import pi

from anglr import Angle

class AngleTestCase(unittest.TestCase):
    def test_construction(self):
        self.assertEqual(str(Angle()), "0 rad", "bad ")
        self.assertEqual(str(Angle(87 * pi / 2)), "136.659280431156 rad", "bad angle")
        self.assertEqual(str(Angle(pi / 2, "radians")), "1.5707963267948966 rad", "bad angle")
        self.assertEqual(str(Angle(Angle(pi / 2, "radians"))), "1.5707963267948966 rad", "bad angle") # same as above
        self.assertEqual(str(Angle(64.2, "degrees")), "1.1205013797803596 rad", "bad angle")
        self.assertEqual(str(Angle(384.9, "gradians")), "6.0459950618335565 rad", "bad angle")
        self.assertEqual(str(Angle(4.5, "hours")), "1.1780972450961724 rad", "bad angle")
        self.assertEqual(str(Angle(203.8, "arcminutes")), "0.059283016926074066 rad", "bad angle")
        self.assertEqual(str(Angle(42352.7, "arcseconds")), "0.2053316839192784 rad", "bad angle")
        self.assertEqual(str(Angle((56, 32), "vector")), "0.5191461142465229 rad", "bad angle") # angle in standard position - counterclockwise from the positive X-axis

    def test_operations(self):
        x = Angle(58.3)
        self.assertEqual("{} {} {} {} {} {} {} {} {} {} {}".format([x], str(x), x.radians, x.degrees, x.gradians, x.hours, x.arcminutes, x.arcseconds, x.vector, x.x, x.y), "[<Angle 58.3 rad>] 58.3 rad 58.3 3340.3439456126994 3711.4932729029993 222.68959637417993 200420.63673676195 12025238.204205718 (-0.17955679797714189, 0.9837476080276871) -0.17955679797714189 0.9837476080276871", "bad conversion")
        self.assertEqual(str(complex(x)), "(58.3+0j)", "bad conversion")
        self.assertEqual(str(float(x)), "58.3", "bad conversion")
        self.assertEqual(str(int(x)), "58", "bad conversion")
        x.radians = pi / 2
        self.assertEqual(str(x.dump()), "<Angle: 1.5707963267948966 radians, 90.0 degrees, 100.0 gradians, 6.0 hours, 5400.0 arcminutes, 324000.0 arcseconds, offset (6.123233995736766e-17, 1.0)>", "bad conversion")
        x.degrees = 64.2
        self.assertEqual(str(x.dump()), "<Angle: 1.1205013797803596 radians, 64.2 degrees, 71.33333333333334 gradians, 4.28 hours, 3852.0 arcminutes, 231120.0 arcseconds, offset (0.4352310993723275, 0.9003187714021935)>", "bad conversion")
        x.gradians = 384.9
        self.assertEqual(str(x.dump()), "<Angle: 6.0459950618335565 radians, 346.40999999999997 degrees, 384.9 gradians, 23.093999999999998 hours, 20784.6 arcminutes, 1247076.0 arcseconds, offset (0.9720020258153625, -0.23497247032542193)>", "bad conversion")
        x.hours = 4.5
        self.assertEqual(str(x.dump()), "<Angle: 1.1780972450961724 radians, 67.5 degrees, 75.0 gradians, 4.5 hours, 4050.0 arcminutes, 243000.0 arcseconds, offset (0.38268343236508984, 0.9238795325112867)>", "bad conversion")
        x.arcminutes = 203.8
        self.assertEqual(str(x.dump()), "<Angle: 0.059283016926074066 radians, 3.396666666666667 degrees, 3.7740740740740746 gradians, 0.22644444444444445 hours, 203.8 arcminutes, 12228.000000000002 arcseconds, offset (0.9982432765393775, 0.05924829823655638)>", "bad conversion")
        x.arcseconds = 42352.7
        self.assertEqual(str(x.dump()), "<Angle: 0.2053316839192784 radians, 11.764638888888886 degrees, 13.071820987654316 gradians, 0.7843092592592591 hours, 705.8783333333331 arcminutes, 42352.69999999999 arcseconds, offset (0.9789934107119936, 0.20389188748574036)>", "bad conversion")
        x.vector = (56, 32)
        self.assertEqual(str(x.dump()), "<Angle: 0.5191461142465229 radians, 29.74488129694222 degrees, 33.04986810771358 gradians, 1.9829920864628148 hours, 1784.6928778165334 arcminutes, 107081.57266899201 arcseconds, offset (0.8682431421244592, 0.49613893835683376)>", "bad conversion")

    def test_operations(self):
        x = Angle((56, 32), "vector")
        self.assertEqual(str(Angle(pi / 6) + Angle(2 * pi / 3)), "2.617993877991494 rad", "bad operation")
        self.assertEqual(str(x * 2 + Angle(3 * pi / 4) / 4 + 5 * Angle(pi / 3)), "6.86332860702412 rad", "bad operation")
        self.assertEqual(str(-abs(+Angle(pi))), "-3.141592653589793 rad", "bad operation")
        self.assertEqual(str(round(Angle(-75.87))), "-76 rad", "bad operation")
        self.assertEqual(str(Angle(-4.3) <= Angle(pi / 4) > Angle(0.118) == Angle(0.118)), "True", "bad operation")

    def test_unit_circle(self):
        self.assertEqual(str(Angle(-870.3, "gradians").normalized()), "32.540085710391615 rad", "bad operation")
        self.assertEqual(str(Angle(-870.3, "gradians").normalized(0)), "32.540085710391615 rad", "bad operation") # same as above
        self.assertEqual(str(Angle(-870.3, "gradians").normalized(0, 2 * pi)), "32.540085710391615 rad", "bad operation") # same as above
        self.assertEqual(str(Angle(-870.3, "gradians").normalized(-pi, pi)), "29.398493056801822 rad", "bad operation")
        self.assertEqual(str(Angle(-870.3, "gradians").normalized(-pi, 0)), "13.128450201606015 rad", "bad operation")
        self.assertEqual(str(Angle(1, "degrees").angle_between_clockwise(Angle(0, "degrees"))), "6.265732014659643 rad", "bad operation")
        self.assertEqual(str(Angle(1, "degrees").angle_between(Angle(0, "degrees"))), "0.017453292519943295 rad", "bad operation")
        self.assertEqual(str(Angle(0, "degrees").angle_within(Angle(-45, "degrees"), Angle(45, "degrees"))), "True", "bad operation")
        self.assertEqual(str(Angle(-1, "degrees").angle_within(Angle(-1, "degrees"), Angle(1, "degrees"), strictly_within=True)), "False", "bad operation")
        self.assertEqual(str(Angle(-1, "degrees").angle_to(Angle(180, "degrees"))), "-3.12413936106985 rad", "bad operation")
        self.assertEqual(str(Angle(0, "degrees").angle_to(Angle(180, "degrees"))), "3.141592653589793 rad", "bad operation")

if __name__ == "__main__":
    unittest.main()
