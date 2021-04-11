import webbrowser, time

link1 = 'http://www.goolge.com'

result = 0

print(' ')

Numper = int(input('\x1b[1;00mEnter the number of points: '))

print(' ')

webbrowser.open(link1)

while True:

    result = result + 50

    if Numper == result:

        print(' ')

        print('\x1b[1;00m-Done successfully \x1b[1;00m-Points', Numper)

        break

    print('\x1b[1;00m⚡Done add 50 points..')

    time.sleep(4)

    webbrowser.open(link1)
