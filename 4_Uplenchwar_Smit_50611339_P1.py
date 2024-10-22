def quickSort(cities, l, h):
    if l < h:
        pivot = partition(cities, l, h)
        quickSort(cities, l, pivot-1)
        quickSort(cities, pivot+1, h)

def partition(cities, l, h):
    #chossing the last element as pivot
    pivot = cities[h]
    #pointer for smaller element
    i = l - 1
    
    for j in range(l, h):
        if (cities[j][1]<pivot[1]) or (cities[j][1] == pivot[1] and cities[j][0]<= pivot[0]):
            i = i + 1
            cities[i], cities[j] = cities[j], cities[i]
    
    cities[i+1], cities[h] = cities[h], cities[i+1]
    return i + 1
    

def ascending_sort(cities):
    # Please write your algorithm here:
    quickSort(cities, 0 , len(cities)-1)

    # .................................
    return cities


def read_input():
    cities = []
    while True:
        city_input = input().strip()
        if not city_input:
            break
        city_info = city_input.split()
        city_index, population = int(city_info[0]), int(city_info[1])
        cities.append((city_index, population))

    return cities


if __name__ == "__main__":
    cities = read_input()
    sorted_cities = ascending_sort(cities)
    for city in sorted_cities:
        print(city[0], city[1])
