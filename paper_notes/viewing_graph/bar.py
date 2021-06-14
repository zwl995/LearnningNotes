import matplotlib.pyplot as plt

# total_width = 0.2
width = 0.2

books_loop_length_list = [3, 4]
books_valid_loop_list = [122, 2]
books_invalid_loop_list = [57, 2]
books_x = list(range(len(books_loop_length_list)))
plt.bar(books_x, books_valid_loop_list, alpha=0.9, width=width, label='valid loop', fc='g')
for i in range(len(books_x)):
    books_x[i] = books_x[i] + width
plt.bar(books_x, books_invalid_loop_list,alpha=0.9,  width=width, label='invalid loop', tick_label=books_loop_length_list, fc='r')
plt.legend()
plt.show()

cereal_loop_length_list = [3, 4, 5]
cereal_valid_loop_list = [71, 0, 1]
cereal_invalid_loop_list = [60, 79, 50]
cereal_x = list(range(len(cereal_loop_length_list)))
plt.bar(cereal_x, cereal_valid_loop_list, alpha=0.9, width=width, label='valid loop', fc='g')
for i in range(len(cereal_x)):
    cereal_x[i] = cereal_x[i] + width
plt.bar(cereal_x, cereal_invalid_loop_list, alpha=0.9, width=width, label='invalid loop', tick_label=cereal_loop_length_list, fc='r')
plt.legend()
plt.show()

cup_loop_length_list = [3, 4, 5, 6, 7, 8]
cup_valid_loop_list = [256, 5, 1, 0, 0, 0]
cup_invalid_loop_list = [84, 42, 34, 34, 48, 4]
cup_x = list(range(len(cup_loop_length_list)))
plt.bar(cup_x, cup_valid_loop_list, alpha=0.9, width=width, label='valid loop', fc='g')
for i in range(len(cup_x)):
    cup_x[i] = cup_x[i] + width
plt.bar(cup_x, cup_invalid_loop_list, alpha=0.9, width=width, label='invalid loop', tick_label=cup_loop_length_list, fc='r')
plt.legend()
plt.show()

desk_loop_length_list = [3, 4, 5, 6]
desk_valid_loop_list = [133, 6, 0, 0]
desk_invalid_loop_list = [85, 55, 7, 2]
desk_x = list(range(len(desk_loop_length_list)))
plt.bar(desk_x, desk_valid_loop_list, alpha=0.9, width=width, label='valid loop', fc='g')
for i in range(len(desk_x)):
    desk_x[i] = desk_x[i] + width
plt.bar(desk_x, desk_invalid_loop_list, alpha=0.9, width=width, label='invalid loop', tick_label=desk_loop_length_list, fc='r')
plt.legend()
plt.show()

fc_loop_length_list = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
fc_valid_loop_list = [535, 14, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
fc_invalid_loop_list = [262, 146, 88, 122, 202, 170, 126, 119, 35, 6, 6, 4]
fc_x = list(range(len(fc_loop_length_list)))
plt.bar(fc_x, fc_valid_loop_list, alpha=0.9, width=width, label='valid loop', fc='g')
for i in range(len(fc_x)):
    fc_x[i] = fc_x[i] + width
plt.bar(fc_x, fc_invalid_loop_list, alpha=0.9, width=width, label='invalid loop', tick_label=fc_loop_length_list, fc='r')
plt.legend()
plt.show()

indoor_loop_length_list = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
indoor_valid_loop_list = [349, 10, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
indoor_invalid_loop_list = [255, 285, 239, 193, 189, 174, 144, 104, 68, 58, 25, 3]
indoor_x = list(range(len(indoor_loop_length_list)))
plt.bar(indoor_x, indoor_valid_loop_list, alpha=0.9, width=width, label='valid loop', fc='g')
for i in range(len(indoor_x)):
    indoor_x[i] = indoor_x[i] + width
plt.bar(indoor_x, indoor_invalid_loop_list, alpha=0.9, width=width, label='invalid loop', tick_label=indoor_loop_length_list, fc='r')
plt.legend()
plt.show()

oats_loop_length_list = [3, 4, 5]
oats_valid_loop_list = [140, 3, 0]
oats_invalid_loop_list = [68, 10, 2]
oats_x = list(range(len(oats_loop_length_list)))
plt.bar(oats_x, oats_valid_loop_list, alpha=0.9, width=width, label='valid loop', fc='g')
for i in range(len(oats_x)):
    oats_x[i] = oats_x[i] + width
plt.bar(oats_x, oats_invalid_loop_list, alpha=0.9, width=width, label='invalid loop', tick_label=oats_loop_length_list, fc='r')
plt.legend()
plt.show()

street_loop_length_list = [3, 4, 5, 6]
street_valid_loop_list = [31, 1, 0, 0]
street_invalid_loop_list = [28, 37, 17, 5]
street_x = list(range(len(street_loop_length_list)))
plt.bar(street_x, street_valid_loop_list, alpha=0.9, width=width, label='valid loop', fc='g')
for i in range(len(street_x)):
    street_x[i] = street_x[i] + width
plt.bar(street_x, street_invalid_loop_list, alpha=0.9, width=width, label='invalid loop', tick_label=street_loop_length_list, fc='r')
plt.legend()
plt.show()

loop_length_list = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
valid_loop_list =   [1637, 41, 4, 1, 0, 0, 0, 0, 0, 0, 0, 0]
invalid_loop_list = [815, 656, 437, 356, 425, 348, 270, 223,103, 64, 31, 7]
x = list(range(len(loop_length_list)))
plt.bar(x, valid_loop_list, alpha=0.9, width=width, label='valid loop', fc='g')
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, invalid_loop_list, alpha=0.9, width=width, label='invalid loop', tick_label=loop_length_list, fc='r')
plt.legend()
plt.show()