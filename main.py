import convert
x=int(input((f"Input distance in km: ")))
y=int(input((f"Input distance in m: ")))

print(f"{x}km is  the same as {convert.km_to_m(x)}m")
print(f"{y}m is  the same as {convert.m_to_km(y)}km")
