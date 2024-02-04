# def scale(data, factor):
#    for val in data:
#        val *= factor

# Explain why or why not

# It will not work properly because the current value in data is copied into val
# which is then scaled by the factor. This does not affect the contents of data