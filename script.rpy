# Compile this code while doing career research.
# ratio raw source code :  act.V/backpack/ratio.rpy

## Joystick Mapper > Dual

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define t = Character("Trinity")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    play music "bliss.ogg" fadein 3.0

    scene taximap
    with dissolve

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show trinity smile

label first_setup:
    default cost = 0
    default savings = 0
    default current_exp = 0
    default exp = 0
    default savings_88 = 0
    default hours_day = 0
    default hourly = 0
    default days_week = 0
    default days_calweek = 0



    default cash = 0
    default accounts = 0
    default invest = 0
    default act_recv = 0

    default rec = 0

    $ savings_88 = renpy.input("How much are you trying to save?", allow="0123456789")
    $ savings_88 = int(savings_88)

    $ savings = renpy.input("How much do you have now?", allow="0123456789")
    $ savings = int(savings)


    "Your daily CoST, or constitution, is currently derived from the formula of capitalism."
    "Will this eventually change?"
    "Only time will tell."

    # Initial setup, 1st prototype.  Enter salary, which determines CoST, or constitution.

    $ hourly = renpy.input("what is your average hourly rate?", allow="0123456789")
    $ hourly = int(hourly)

    $ hours_day = renpy.input("how many hours a day do you work?", allow="0123456789")
    $ hours_day = int(hours_day)




    $ days_week = renpy.input("How many working days are in your pay period?", allow="0123456789")
    $ days_week = int(days_week)

    $ days_calweek = renpy.input("And finally, how many calendar days are in your pay period?", allow="0123456789")
    $ days_calweek = int(days_calweek)


    $ cost = (hourly*hours_day*days_week)/(days_calweek)
    $ cost = int(cost)

    hide trinity smile

    # In layman's terms, CoST is defined as the average salary divided by days left in financial period... or something like that.

label exp_zero:

    $ current_exp = 0

# Then to the main menu.

# ReST is displayed as (Average CoST - today's expenses) / (Average CoST).
label main_menu:

    default rest = 0

    $ rest = cost - current_exp

    "Working [hours_day] for [hourly] per hour running [days_week] of [days_calweek], your HP is [cost]."



    # Main menu is here.
    menu:

        "Your current assets are [savings].  ReST is [rest] out of [cost].  Today's EXP is [current_exp]."

        "Manage EXP.":
            jump manage

        "Reconcile.":
            jump reconcile

        "Reset.":
            jump start

        "Exit.":
            jump end




label manage:

    menu:

        "What do you wish to do with current EXP?"

        "Add/change.":
            jump change_exp

        "Reset.":
            jump reset_exp

        "Go back one level.":
            jump main_menu


label change_exp:

# Input, and == command.
    menu:

        "Add EXP.":
            jump add_exp

        "Change EXP.":
            jump chg_exp

        "Return to main menu.":
            jump main_menu



label add_exp:

    $ exp_plus = renpy.input("How much to add?", allow="0123456789")
    $ exp_plus = int(exp_plus)

    $ current_exp += exp_plus

    jump main_menu


label chg_exp:

    $ exp_chg = renpy.input("What is today's total expenditures?", allow="0123456789")
    $ exp_chg = int(exp_chg)

    $ current_exp == exp_chg

    jump main_menu



label reset_exp:

    menu:

        "Are you sure you want to reset today's EXP?"

        "Yes.":
            jump reset_yes

        "No.":
            jump manage

label reset_yes:

    jump exp_zero


label reconcile:

    menu:

        "What do you wish to reconcile?"

        "Reconcile savings.":
            jump savings

        "Reconcile goal.":
            jump goal


label savings:

    $ cash = renpy.input("How much do you have now?", allow="0123456789")

    $ cash = int(cash)

    $ savings = cash

    jump main_menu


label goal:


    menu:

        "Are you sure you want to move the goal posts?"

        "Yes.":
            jump yes

        "No.":
            jump main_menu




label yes:

    $ savings_88 = renpy.input("What is your new goal?", allow="0123456789")

    $ savings_88 = int(savings_88)

    jump main_menu



label end:
# This ends the game.
return
