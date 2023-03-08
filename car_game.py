command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car already started")
        else:
            started = True
            print("Car  started")
    elif command == "stop":
        if not started:
            print("Car already stopped")
        else:
            started = False
            print("car stopped")
    elif command == "help":
        print("""
        star - to start car
        stop - to stop car
        quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print("Sorry i dont understand")