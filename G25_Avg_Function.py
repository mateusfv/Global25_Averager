def g25_average(input):
    with open(input, "r") as input_coords:
        all_coords = [i * 0.0 for i in range(0, 25)]
        counter = 0
        for line in input_coords.readlines():
            counter += 1
            list = line.split(",")
            list = [float(i) for i in list[1:]]
            all_coords[0] = all_coords[0] + list[0]
            all_coords[1] = all_coords[1] + list[1]
            all_coords[2] = all_coords[2] + list[2]
            all_coords[3] = all_coords[3] + list[3]
            all_coords[4] = all_coords[4] + list[4]
            all_coords[5] = all_coords[5] + list[5]
            all_coords[6] = all_coords[6] + list[6]
            all_coords[7] = all_coords[7] + list[7]
            all_coords[8] = all_coords[8] + list[8]
            all_coords[9] = all_coords[9] + list[9]
            all_coords[10] = all_coords[10] + list[10]
            all_coords[11] = all_coords[11] + list[11]
            all_coords[12] = all_coords[12] + list[12]
            all_coords[13] = all_coords[13] + list[13]
            all_coords[14] = all_coords[14] + list[14]
            all_coords[15] = all_coords[15] + list[15]
            all_coords[16] = all_coords[16] + list[16]
            all_coords[17] = all_coords[17] + list[17]
            all_coords[18] = all_coords[18] + list[18]
            all_coords[19] = all_coords[19] + list[19]
            all_coords[20] = all_coords[20] + list[20]
            all_coords[21] = all_coords[21] + list[21]
            all_coords[22] = all_coords[22] + list[22]
            all_coords[23] = all_coords[23] + list[23]
            all_coords[24] = all_coords[24] + list[24]
    print("Sum: \n", all_coords)
    print("Samples: ", counter)
    avg_float = []
    for pc in all_coords:
        avg_float.append(pc/counter)
    avg_float = [round(i, 7) for i in avg_float]
    avg_float = [str(i) for i in avg_float]
    avg_string = ",".join(avg_float)
    average = "New_Average," + avg_string
    print("Output: \n" + average)
    with open("output.txt", "w") as output_coords:
        output_coords.write(average)
