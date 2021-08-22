started = False
while True:

    car_action = input('What do yo want to do with the car: ').upper()

    if car_action == 'START':
        if started:
            print('Car is already started')
        else:
            print('Car has been started and it is ready to go.')
            started = True

    elif car_action == 'STOP':

        if not started:
            print('Car has already been stopped')
        else:
            print('The car has been stopped')
            started = False

    elif car_action == 'QUIT':
        print('You have quitted the car')
        break

    elif car_action == "HELP":
        print('''
start: to start the car
stop: to sotop the car
quit: to quit the car
        ''')
    else:
        print('I do not understand what you mean')
