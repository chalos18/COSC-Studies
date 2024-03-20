def which_segments(city_map):
    """
        Takes the map of the city and returns the list of road segments that
        must be cleared so that there is a clear path between any two locations and the total
        length of the cleaned-up road segments is minimised

        Undirectted weighted graph, each vertex is one location in the city. 
        Each two way road segment is represented as an edge which connects two locations together
        and the weight of the edge is the length of road segment

        The given city has at least one location
        There is a path between any two locations

        The output is a list of orad segments that must be cleared
        Each segment is a tuple of two lcoation numbers
        The smaller number should appear first.
        If the solution is not unique, it does not matter which solution is returned by the function
    """