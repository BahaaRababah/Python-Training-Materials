raw_sensor_data = [15.5, -2.0, 18.1, 0.0, -99.9, 22.4]
valid_data=list(filter(lambda x:x>=0.0,raw_sensor_data))
calibrated_data=list(map(lambda x:x*1.5,valid_data))

print(f"Original data: {raw_sensor_data}")
print(f"Valid data: {valid_data}")
print(f"Calibrated data: {(calibrated_data):.2f}")