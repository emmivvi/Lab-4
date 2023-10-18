#set first device
uart = UART(1, baudrate=9600, tx=Pin(8), rx=Pin(9))
uart.init(bits=8, parity=None, stop=1)

#set second device
uart2 = UART(2, baudrate=9600, tx=Pin(8), rx=Pin(9))
uart2.init(bits=8, parity=None, stop=1)

colour = "red"

while True:
    match colour:
   
        case "red"  : #stoplight until the other light is also red
#            LED on (red)
            if other stop == red:
                colour = "green"
         
        case "green" : #greenlight and extended greenlight if no cars on the other stop's sensor
#            LED on (green)
            sleep(5)
            if other stop sensor == full:
                colour = "yellow"
            else:
                sleep(5)
                colour = "yellow"
                
        case "yellow" : #yellow light between green and red
#            LED on (yellow)
            sleep(3)
            colour = "red"

        case _  : 
              print("error")

