import graph_point
p1 = graph_point.p1
p2 = graph_point.p2

def restart():
    restart = input("\nDo you want to do another operation with the same points? (y/n)")

    if restart == 'y' or restart == 'Y':
        pick_func()
    else:
        exit


def pick_func():
    input_function = input("\nSelect which Function you wish to use by pressing the number corrosponding to the function: \n 1: Print Point \n 2: distance between point 2 and center \n 3: distance between points 1 and 2 \n 4: slope between 2 points \n 5: slope from center\n 6: area between 2 points\n 7: area from center\n 8: smallest angle\n 9: the y intercept\n")

    if input_function == '1':
        print(graph_point.graph_point.print_point(p1))
    elif input_function == '2':
        print(graph_point.graph_point.distance_from_center(p2))
    elif input_function == '3':
        print(graph_point.graph_point.distance_from_another_point(p1,p2))
    elif input_function == '4':
        print(graph_point.graph_point.slope_between_2_points(p1,p2))
    elif input_function == '5':
        print(graph_point.graph_point.slope_from_center(p1))
    elif input_function == '6':
        print(graph_point.graph_point.area_from_another_point(p1,p2))
    elif input_function == '7':
        print(graph_point.graph_point.area_from_center(p1))
    elif input_function == '8':
        print(graph_point.graph_point.smallest_angle(p1,p2))
    elif input_function == '9':
        print(graph_point.graph_point.y_int(p1,p2))
    restart()

pick_func()





