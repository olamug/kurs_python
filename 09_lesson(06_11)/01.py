graph = [
    [0, 1, 0, 0, 0, 1, 1],
    [1, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 0, 1],
    [0, 0, 1, 0, 1, 0, 0],
    [0, 0, 1, 1, 0, 1, 0],
    [1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 1, 0]
]

list = ["home", "school", 'hospital', 'theatre', 'cinema', 'church', 'bar']

for row in range(len(graph)):
    print(list[row], ":")
    for col in range(len(graph[row])):
        if graph[row][col] == 1:
            print(list[row], "---", list[col])



