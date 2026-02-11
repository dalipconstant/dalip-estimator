# Dalip estimator (simple version)

D = 1.09e11
G = 6.6743e-11

ARCSEC_PER_RAD = 206265
ARCSEC_PER_DEG = 3600


# ---- ADDED FUNCTION (no changes to existing logic) ----
def estimate_g(LB_arcsec, b_m, D=1.09e11):
    """
    Estimate gravitational acceleration using the empirical relation.
    Parameters:
        LB_arcsec : light bending in arcseconds
        b_m       : impact parameter in meters
    Returns:
        g (m/s^2)
    """
    return (LB_arcsec * D) / b_m


# ---- INPUT ----
lb = float(input("Light bending value: "))
lb_unit = input("Unit (arcsec/rad/deg): ")

b = float(input("Impact parameter: "))
b_unit = input("Unit (m/km/au/rsun/ly): ")


# ---- CONVERSIONS ----
if lb_unit == "rad":
    lb *= ARCSEC_PER_RAD
elif lb_unit == "deg":
    lb *= ARCSEC_PER_DEG

if b_unit == "km":
    b *= 1000
elif b_unit == "au":
    b *= 1.496e11
elif b_unit == "rsun":
    b *= 6.957e8
elif b_unit == "ly":
    b *= 9.461e15


# ---- CALCULATIONS ----
g = (lb * D) / b
M = g * b * b / G

print("\nResults:")
print("g =", g, "m/s^2")
print("Mass =", M, "kg")
