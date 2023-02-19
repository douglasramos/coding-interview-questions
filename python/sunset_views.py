# Sunset Views
# Given an array of buildings and a direction that all of the buildings face, return an array of the indices of the buildings that can see the sunset.
# A building can see the sunset if it's strictly taller than all of the buildings that come after it in the direction that it faces.
# The input array named buildings contains positive, non-zero integers representing the heights of the buildings. A building at indexi thus has a height denoted by buildings[i].
# All of the buildings face the same direction, and this direction is either east or west, denoted by the input string named direction, which will always be equal to either "EAST" or
# "WEST". In relation to the input array, you can interpret these directions as right for east and left for west.
# Important note: the indices in the ouput array should be sorted in ascending order.
# Sample Input #1
# buildings = [3, 5, 4, 4, 3, 1, 3, 2]
# direction = "EAST"
# Sample Output #1
# [1, 3, 6, 7]


def peek(stack):
    return stack[len(stack)-1]

def sunset_views(buildings, direction):
    #  rename to better reflect what the array represents
    buildingHeights = buildings

    if len(buildings) == 0: return []

    # indices = buildings numbers. Index 0 = Building 0 ....
    buildingsWithView = [0 if direction == "EAST" else len(buildingHeights)-1]
    for index in range(1, len(buildingHeights)) if direction == "EAST" else range(len(buildingHeights)-2, -1, -1):
        while len(buildingsWithView) > 0 and buildingHeights[index] >= buildingHeights[peek(buildingsWithView)]:
            buildingsWithView.pop()
        buildingsWithView.append(index)

    if direction == "WEST": buildingsWithView.reverse()    
        
    return buildingsWithView


print(sunset_views([3, 5, 4, 4, 3, 1, 3, 2], "WEST"))