def get_temp_input():
    temperature = float(input('Enter Temperature: '))
    return temperature + 273 if temperature < 273 else temperature
    
def get_inputs(choice):
    values = []
    if choice != 'p': values.append(float(input('Enter Pressure: ')))
    if choice != 'v': values.append(float(input('Enter Volume: ')))
    if choice != 'n': values.append(float(input('Enter Moles: ')))
    if choice != 't': values.append(get_temp_input())
    return values

formula_lookup = {
    'p': lambda volume,moles,temperature:    (moles*temperature*0.0821)/volume,
    'v': lambda pressure,moles,temperature:  (moles*temperature*0.0821)/pressure,
    'n': lambda pressure,volume,temperature: (pressure*volume)/(temperature*0.0821),
    't': lambda pressure,volume,moles:       (pressure*volume)/(moles*0.0821) }

print("Ideal Gas Law Solver (PV=nRT)")
choice = input("Enter Option(p/v/n/t): ")

if choice in formula_lookup:
    print( formula_lookup[choice]( *get_inputs(choice) ) )
else:
    print('Invalid Input')