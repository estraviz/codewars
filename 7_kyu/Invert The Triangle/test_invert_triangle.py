from invert_triangle import invert_triangle


def test_invert_triangle():
    triangle = "           ##           \n          ####          \n         ######         \n        ########        \n       ##########       \n      ############      \n     ##############     \n    ################    \n   ##################   \n  ####################  \n ###################### \n########################\n"
    inverted = "\n                        \n#                      #\n##                    ##\n###                  ###\n####                ####\n#####              #####\n######            ######\n#######          #######\n########        ########\n#########      #########\n##########    ##########\n###########  ###########"
    assert invert_triangle(triangle) == inverted

    triangle = "  #  \n ### \n#####\n"
    inverted = "\n     \n#   #\n## ##"
    assert invert_triangle(triangle) == inverted

    triangle = "   ##   \n  ####  \n ###### \n########\n"
    inverted = "\n        \n#      #\n##    ##\n###  ###"
    assert invert_triangle(triangle) == inverted

    triangle = "###  ###\n##    ##\n#      #\n        \n"
    inverted = "\n########\n ###### \n  ####  \n   ##   "
    assert invert_triangle(triangle) == inverted

    triangle = "        #        \n       ###       \n      #####      \n     #######     \n    #########    \n   ###########   \n  #############  \n ############### \n#################\n"
    inverted = "\n                 \n#               #\n##             ##\n###           ###\n####         ####\n#####       #####\n######     ######\n#######   #######\n######## ########"
    assert invert_triangle(triangle) == inverted

    triangle = "#####  #####\n####    ####\n###      ###\n##        ##\n#          #\n            \n"
    inverted = "\n############\n ########## \n  ########  \n   ######   \n    ####    \n     ##     "
    assert invert_triangle(triangle) == inverted

    triangle = "     ##     \n    ####    \n   ######   \n  ########  \n ########## \n############\n"
    inverted = "\n            \n#          #\n##        ##\n###      ###\n####    ####\n#####  #####"
    assert invert_triangle(triangle) == inverted

    triangle = "       ##       \n      ####      \n     ######     \n    ########    \n   ##########   \n  ############  \n ############## \n################\n"
    inverted = "\n                \n#              #\n##            ##\n###          ###\n####        ####\n#####      #####\n######    ######\n#######  #######"
    assert invert_triangle(triangle) == inverted

    triangle = "#############  #############\n############    ############\n###########      ###########\n##########        ##########\n#########          #########\n########            ########\n#######              #######\n######                ######\n#####                  #####\n####                    ####\n###                      ###\n##                        ##\n#                          #\n                            \n"
    inverted = "\n############################\n ########################## \n  ########################  \n   ######################   \n    ####################    \n     ##################     \n      ################      \n       ##############       \n        ############        \n         ##########         \n          ########          \n           ######           \n            ####            \n             ##             "
    assert invert_triangle(triangle) == inverted
