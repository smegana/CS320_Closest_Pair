def closest_pair():
    def squared(x): return x*x
    def distance(a, b): return math.sqrt(squared(a[0]-b[0]) + squared(a[1]-b[1]))

    def brute_force(P):
        L = len(P)
        float minDist = 999999999999;
        for x in range(1, L):
            for y in range(2, L):
                 if(minDist > distance(x, y)):
                    minDist = distance(x, y)
        return minDist
        
    def write_to_file(closest, filename):
        with open("output_" + filename, mode='w') as f:
            for id1, id2 in edges:
                f.write("() ()\n".format(id1, id2))



