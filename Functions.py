"""
El Hadji Omar Bane
Creating and using Functions in Python
9/26/2022
"""
import os

ENDING_PAGE = 0


# retrieves the user's input
def get_integer_input(lowest_input: int, highest_input: int) -> int:
    inputted_value = int(input("Enter input:"))

    # loops until the user gives a valid input
    while lowest_input > inputted_value or inputted_value > highest_input:
        print("Invalid input. Try again.")
        inputted_value = int(input("Enter input:"))
    return inputted_value


# lists numbered elements for
def display_numbered_elements(*options: str):
    for option_i in range(len(options)):
        print(f"{option_i + 1}. {options[option_i]}")


# gets a specific output based on the input
def get_designated_input_outputs(*outputs: int) -> int:
    i = get_integer_input(1, len(outputs)) - 1
    return outputs[i]


# tells the user where the story is from
def introduction():
    print("This story was made by the creators of the Elder's Scroll franchise.")
    print("Source: https://en.uesp.net/wiki/Skyrim:Kolb_%26_the_Dragon")


# returns the next page's number
def pg1() -> int:
    print('Kolb was a brave Nord warrior. One day his Chief asked Kolb to slay an evil dragon that threatened their \n'
          'village. "Go through the mountain pass, Kolb", his Chief said. "You will find the Dragon on the other \n'
          'side."')
    input("Press Enter to continue")
    return 2


def pg2() -> int:
    print("Kolb took his favorite axe and shield and walked to the pass, where he found a cold cave, a windy cave,\n"
          "and a narrow trail.")
    display_numbered_elements("Enter the cold cave", "Enter the windy cave", "Walk up the trail")
    return get_designated_input_outputs(17, 8, 12)


def pg3() -> int:
    print("Kolb stepped onto a rocky hill. He could see the dragon sleeping below, and a tavern off a road nearby.")
    display_numbered_elements("Climb down", "Visit tavern")
    return get_designated_input_outputs(16, 14)


def pg4() -> int:
    print("Treading through the marsh, Kolb discovered a wailing ghost blocking his way.")
    display_numbered_elements("Raise Shield", "Swing Axe")
    return get_designated_input_outputs(9, 13)


def pg5() -> int:
    print("Treading through the marsh, Kolb discovered a wailing ghost blocking his way.")
    display_numbered_elements("Attack Ghost", "Give Gold")
    return get_designated_input_outputs(15, 10)


def pg6() -> int:
    print("The head of the axe lodged itself in the tough, scaly neck of the beast. It wailed and thrashed, but Kolb \n"
          "held on and eventually sawed through the neck, killing the beast. Kolb returned home victorious, and his \n"
          "village was never bothered by the dragon again.")
    return ENDING_PAGE


def pg7() -> int:
    print("Leaving the marsh behind him, Kolb could see the dragon's lair nearby, as well as a small, welcoming \n"
          "tavern.")
    display_numbered_elements("Go to the Lair", "Go to Tavern")
    return get_designated_input_outputs(16, 14)


def pg8() -> int:
    print("A strong gust of wind blew Kolb's torch out, and knocked him into a pit where split his head and \n"
          "died.")
    return ENDING_PAGE


def pg9():
    print("The orc cackled as his club splintered Kolb's shield and smashed into his face. There Kolb died, and the \n"
          "orc had soup from his bones.")
    return ENDING_PAGE


def pg10() -> int:
    print("Kolb remembered a story his Gran told him and tossed two gold chits for the ghost, and it faded away, \n"
          "allowing him to pass.")
    input("Press Enter to continue")
    return 7


def pg11() -> int:
    print("Kolb crept towards the belly of the beast, but no sooner had he taken his eyes off the head of the beast \n"
          "than it snapped him up and ate him whole, axe and all.")
    return ENDING_PAGE


def pg12() -> int:
    print("Climbing up, Kolb found a camp. He met a wise man who shared bread and showed two paths to the dragon's \n"
          "lair. One went through the hills, the other through a marsh.")
    display_numbered_elements("Take the hills", "Take the marsh")
    return get_designated_input_outputs(3, 5)


def pg13() -> int:
    print("Before the orc could strike, Kolb swung his mighty axe. The orc's head and club fell uselessly to the \n"
          "floor.")
    input("Press Enter to continue")
    return 3


def pg14() -> int:
    print("Kolb stopped at the tavern to rest before fighting the dragon. High elves ran the tavern, however, and \n"
          "poisoned his mead so they could steal his gold.")
    return ENDING_PAGE


def pg15() -> int:
    print("Kolb swung his axe as hard as he could, but the ghost hardly seemed to notice. The ghost drifted into \n"
          "Kolb, and a deep sleep took him over, from which he never awoke.")
    return ENDING_PAGE


def pg16() -> int:
    print("Kolb found the lair where the dragon slept, tendrils of smoke wafting from it's [sic] nostrils. The air \n"
          "made Kolb's eyes sting, and he nearly slipped on the bones of men, picked clean. The beast lay on its \n"
          "side, the throat and belly both waiting targets.")
    display_numbered_elements("Strike the Neck", "Strike the Belly")
    return get_designated_input_outputs(6, 11)


def pg17() -> int:
    print("Kolb stepped into the frozen cave, but his Nord blood kept him warm. A smelly tunnel climbed ahead of him,\n"
          " and wind howled from another to his left. A ladder was nearby as well.")
    display_numbered_elements("Take the smelly tunnel", "Take the windy tunnel", "Climb the ladder")
    return get_designated_input_outputs(4, 8, 12)


def conclusion_prompt():
    input("The End...")
    os.system("cls")


if __name__ == "__main__":
    introduction()

    isRunning = True
    # starts on page 1
    currentPage = 1

    # plays the game until the player reaches one of the endings or an error occurs
    while isRunning:
        print()
        if currentPage == 1: currentPage = pg1()
        elif currentPage == 2: currentPage = pg2()
        elif currentPage == 3: currentPage = pg3()
        elif currentPage == 4: currentPage = pg4()
        elif currentPage == 5: currentPage = pg5()
        elif currentPage == 6: currentPage = pg6()
        elif currentPage == 7: currentPage = pg7()
        elif currentPage == 8: currentPage = pg8()
        elif currentPage == 9: currentPage = pg9()
        elif currentPage == 10: currentPage = pg10()
        elif currentPage == 11: currentPage = pg11()
        elif currentPage == 12: currentPage = pg12()
        elif currentPage == 13: currentPage = pg13()
        elif currentPage == 14: currentPage = pg14()
        elif currentPage == 15: currentPage = pg15()
        elif currentPage == 16: currentPage = pg16()
        elif currentPage == 17: currentPage = pg17()
        elif currentPage == ENDING_PAGE:  # the program has ended
            conclusion_prompt()
            isRunning = False

        # something unexpected happened
        else:
            print("Error Occurred")
            isRunning = False
