# this console is made by @mr-rathi-official001 in class 8.
# this line imports ctime for making the time function to work showing current time.
from time import ctime
# this line imports sleep to add a pause between selected text or functions.
from time import sleep

# ? this console is free to use but credits are required.

# list of all functons in PY-DOS.
# 1. len
# 2. datatype
# 3. reverse
# 4. lower
# 5. upper
# 6. temp;f:c
# 7. temp;c:f
# 8. exit
# 9. credits
# 10. list

# INTRODUCTION
print("welcome to PY-DOS.\nIt is a open source python console"), (sleep(0.2))
print("try typing 'list' or 'credits'. ")

# varible for showing the starting of a new line.
lineSymbol = ("\n~>> ")
# varible for showing the starting of a input varible.
varSymbol = ("v: ")

while 1 > 0:  # loop statements for unlimited working on functions.
    # functionInput varible for getting an input form the user as a function.
    functionInput = input(lineSymbol)
    # conditional staments for the input/output.
    if functionInput == "len":
        # var1 varible as an input form user for the function to start working.
        var1 = input(varSymbol)
        # this function is used to output the total number of characters given as input.
        print(len(var1), " characters")
    else:
        # datatype function is used to show which type of data the given input is.
        if functionInput == "datatype":
            var1 = input(varSymbol)
            print("<<:", type(var1))
        else:
            # reverse function is used to reverse a given input.
            if functionInput == "reverse":
                var1 = str(input(varSymbol))
                print("<<:", var1[::-1])
            else:
                # lower function is used just to convert all the characters of given input into lowercase characters.
                if functionInput == "lower":
                    var1 = str(input(varSymbol))
                    print("<<:", var1.lower())
                else:
                    # upper function is used to convert all the characters of given input into uppercase characters.
                    if functionInput == "upper":
                        var1 = input(varSymbol)
                        print("<<:", var1.upper())
                    else:
                        # temp;f:c function is used to convert given number input as a farehnheight temperature  to celcius temperature.
                        if functionInput == "temp;f:c":
                            fahr_temp = float(input(varSymbol))
                            print("celsius temperature:",
                                  (fahr_temp - 32.0) * 5.0 / 9.0, ' F')
                        else:
                            # temp;c:f function is used to convert the given number input as a celcius temperature  to farehgeigth temperature.
                            if functionInput == "temp;c:f":
                                cels_temp = float(input(varSymbol))
                                print("fahrenheit temprature:",
                                      (cels_temp + 32.0) / 5.0 * 9.0, ' C')
                            else:
                                if functionInput == "exit":  # exit function is used to exit the console.
                                    print("""[TERMINAL{ver:1.0/}
                    MADE BY:s
                            @mr-rathi-official-001
                        ~~~~~~~:)~~~~~~~
                    EXIT CODE: 1"""), (sleep(1.0))
                                    print("exiting TERMINAL:")
                                    break
                                else:
                                    if functionInput == "time":  # time function is used to show the current time.
                                        print("time :\t ", ctime())
                                    else:
                                        # credits function is used to show all the people and resorses used in making this code.
                                        if functionInput == "credits":
                                            print("credits:"), (sleep(1.0))
                                            print("\tThis project was made by @mr-rathi-official001 in the year 2022 in class 8.\n \t Thanks to GITHUB for a platform to publish this project for free. \n \t Thanks to MICROSOFT as most of the ideas of the features for this project came from their softwares. \n \t Thanks to the STACKIO and their community for solving my problems. \n \t Thanks to SOLOLERN.COM and CODE WITH HARRY for their free courses on python. \n \t And at last but not the least thanks to all how made their contribution on this project.")
                                        else:
                                            # this function shows the list of all the function that are valid by this console.
                                            if functionInput == "list":
                                                print(
                                                    "list of all the funtion that are valid for this console."), (sleep(0.5))
                                                print(
                                                    '1. len\n2. dataTypes\n3. reverse\n4. lower\n5. upper\n6. temp;f:c\n7. temp;f:c\n8. credits\n9. exit\n10. list')
