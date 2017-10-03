def draw_stars(arr):
    for i in arr:
        num = ""
        for j in range(0, i):
            num += "*"
        print num

x = [4, 6, 1, 3, 5, 7, 25]

draw_stars(x)

def better_draw_stars(arr):
    for i in arr:
        num = ""
        if type(i) == str:
            first = i[0].lower()
            count = len(i)
            for j in range(0, count):
                num += first
        else:
            first = "*"
            for j in range(0, i):
                num += first
        print num

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
better_draw_stars(x)