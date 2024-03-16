def format_sequence(converters_info, source_format, destination_format):
    """
    Returns the shortest sequence of formats(and therefore converters) required in order to convert a video from the source to the destination format
    1. Input -
    converters_info: string representation of a directed graph, each vertex is a video format. The number of vertices is the number of possible video formats.
    For each converter that is available to the producer, there is an edge from the input format of the converter to the output format of the converter
    source_format: a natural number that specifies the format of the original video
    destination_format: a natural number that specifies the desired format
    """
    pass


converters_info_str = """\
D 2
0 1
"""

source_format = 0
destination_format = 1

a = format_sequence(converters_info_str, source_format, destination_format)
print(a)
assert a == [0, 1]

converters_info_str = """\
D 2
0 1
"""

b = format_sequence(converters_info_str, 1, 1)
print(b)
assert b == [1]

converters_info_str = """\
D 2
0 1
"""

c = format_sequence(converters_info_str, 1, 0)
assert c == "No solution!"

converters_info_str = """\
D 5
1 0
0 2
2 3
1 2
"""

d = format_sequence(converters_info_str, 1, 2)
print(d)
assert d == [1, 2]

converters_info_str = """\
D 1
"""

e = format_sequence(converters_info_str, 0, 0)
print(e)
assert e == [0]
