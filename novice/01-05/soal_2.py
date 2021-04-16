import statistics

# 1. fungsi List
my_list = ['djarum', 'surya', 'gudang garam', 'samsoe']
x = len(my_list)

print(x)

print("")

# 2.
kalimat = "Corona cepat selesai"
y = kalimat.upper()
count_chars = kalimat.count('e')

print(f'To UPPERCASE: {y}, Amiiin!!!!')
print(f"Total 'e' chars in 'kalimat' are {count_chars}")

print("")

# 3. 
obj_list = [11.25, 18.0, 20.0, 10.75, 9.50]
def mean_list(inp_list):
    return statistics.mean(inp_list)

print(mean_list(obj_list))

print("")

# 4.
obj_list = [2, 4, 5, 6]
obj_penambah = [1, 2, 3]
def kali_list(x, y):
    return x + y

print(kali_list(obj_list, obj_penambah))