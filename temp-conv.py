print ('What unit of temperature would you like to convert from?')
choice = input("Choose a unit: K, F, or C: ")
temp = int(input("Enter temperature: "))

if choice is 'K':
    C = temp - 273
    F = C * (9 / 5) + 32
    print('Celcius' + str(C))
    print('Farrenheight: ' + str(F))

if choice is 'F':
    C = (5 / 9) * (temp - 32)
    K = C + 273
    print('Kelvin: ' + str(K))
    print('Celcius: ' + str(C))

if choice is 'C':
    K = temp + 273
    F = temp * (9 / 5) + 32
    print('Kelvin: ' + str(K))
    print('Farrenheight: ' + str(F))