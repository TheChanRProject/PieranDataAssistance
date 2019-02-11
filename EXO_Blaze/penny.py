def roundPartial (value, resolution):
    return round(round(value / resolution) * resolution, 2)

def nickel(l):
    return [f"${roundPartial(i, 0.05)}" for i in l]

print(nickel([10.33, 10.36, 10.67, 10.68, 10.65]))
