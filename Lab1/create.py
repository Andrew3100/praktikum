for i in range(1, 19):
    my_file = open("Variant" + str(i) + ".py", "w+")
    my_file.write("# " + str(i))
    my_file.close()

