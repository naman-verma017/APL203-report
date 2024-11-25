import math
import numpy

class DoublePendulumLagrangian:
    def __init__(self, g, m1, m2, t1, t2, w1, w2, L1, L2):
        self.g = g
        self.m1 = m1
        self.m2 = m2
        self.t1 = t1
        self.t2 = t2
        self.w1 = w1
        self.w2 = w2
        self.L1 = L1
        self.L2 = L2

    def potential_energy(self):
        y1 = -self.L1 * math.cos(self.t1)
        y2 = y1 - self.L2 * math.cos(self.t2)
        return self.m1 * self.g * y1 + self.m2 * self.g * y2

    def kinetic_energy(self):
        K1 = 0.5 * self.m1 * (self.L1 * self.w1) ** 2
        K2 = 0.5 * self.m2 * (
            (self.L1 * self.w1) ** 2
            + (self.L2 * self.w2) ** 2
            + 2 * self.L1 * self.L2 * self.w1 * self.w2 * math.cos(self.t1 - self.t2)
        )
        return K1 + K2

    def mechanical_energy(self):
        return self.kinetic_energy() + self.potential_energy()

    def lagrange_rhs(self, t1, t2, w1, w2):
        
        a1 = (self.L2 / self.L1) * (self.m2 / (self.m1 + self.m2)) * math.cos(t1 - t2)
        a2 = (self.L1 / self.L2) * math.cos(t1 - t2)
        f1 = -(self.L2 / self.L1) * (self.m2 / (self.m1 + self.m2)) * (w2 ** 2) * math.sin(t1 - t2) - \
             (self.g / self.L1) * math.sin(t1)
        f2 = (self.L1 / self.L2) * (w1 ** 2) * math.sin(t1 - t2) - (self.g / self.L2) * math.sin(t2)

        g1 = (f1 - a1 * f2) / (1 - a1 * a2)
        g2 = (f2 - a2 * f1) / (1 - a1 * a2)
        return numpy.array([w1, w2, g1, g2])

    def time_step(self, dt):
        
        y = numpy.array([self.t1, self.t2, self.w1, self.w2])
        k1 = self.lagrange_rhs(*y)
        k2 = self.lagrange_rhs(*(y + dt * k1 / 2))
        k3 = self.lagrange_rhs(*(y + dt * k2 / 2))
        k4 = self.lagrange_rhs(*(y + dt * k3))

        R = (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
        self.t1 += R[0]
        self.t2 += R[1]
        self.w1 += R[2]
        self.w2 += R[3]
