# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.


class percolation:

    def __init__(self, n):
        self.grid = [[-7]]  # For Virtual Top site
        # hashmap = {}
        for i in range(1, n + 1):
            self.grid.append([-2])
            for j in range(n):
                self.grid[i].append(-1)  # -1 denoting a closed site
                # hashmap[(i-1)*n + j+1] = (i,j+1)
            self.grid[i].append(-3)
        self.grid.append([100])  # For Virtual Bottom site
        # print(hashmap)

    # Setting the opensites as a global variable defined inside the class
    opensites = 0

    # ADD ALARMING VALUES FOR INDICES

    def open(self, r, c):
        N = self.n
        if r < 1 or r > N - 2:
            print('Alarm for r', r)
        if c < 1 or c > N - 2:
            print('Alarm for c', c)
        if r == 0 and c > 0:
            print('In Open, Alarm for -7 one', r, c)
        if c == N - 1 and r > 0:
            print('In Open, Alarm for 100 one', r, c)

        if r not in range(1, self.n - 1) or c not in range(1, self.n - 1):
            print('Invalid Indices:', r, c)
            return None

        if self.grid[r][c] == -1:
            # Can't set it to a common indistinguishable value like 0, because
            # we do need to maintain separate connected components for various
            # paths which may be connecting the top to the bottom.
            self.grid[r][c] = (r - 1) * (N - 2) + c
            # Set the default value for an open site as it's own indexpair
            # print("Opened the site [" + str(r) + "," + str(c) + ']', self.grid[r][c])

            # MAJOR UPDATION
            # We are setting the values of such top and bottom grid sites as -7 and 27 after they're opened. So if these sites are closed, they'll contain the regular value i.e. -1. This would also help us in the further cases wherein we need to check whether a site is open or not, we can keep on doing that with the check flag as -1.
            if r == 1:
                self.grid[r][c] = -7
            if r == self.n - 2:
                self.grid[r][c] = 100

            # print('this',self.grid[r][c])
            self.opensites += 1

        else:
            # print('Site is already open')
            return None
            # return False

        # self.n = 7
        # self.union(r,c,self.n)
        self.union(r, c)
        # print(self.grid[r][c], 'Addendum')

    def union(self, r, c):
        # Set the unionable value to itself in case the top or adjacent sites
        # are closed. This value shall come in handy for the 1-down Union exe.
        store0, store1 = [r, c]

        # Set the value of n via the global class variable
        N = self.n
        if r < 1 or r > N - 2:
            print('Alarm for r', r)
        if c < 1 or c > N - 2:
            print('Alarm for c', c)
        if r == 0 and c > 0:
            print('In Union,Alarm for -7 one', r, c)
        if r == N - 1 and c > 0:
            print('In Union,Alarm for 100 one', r, c)

        # store0, store1 = self.findroot(r,c)
        if r > 1 and self.grid[r - 1][c] != -1:
            # print('Case1')
            # MAJOR UPDATION
            # if r == 2 :
            #    self.grid[r][c] = -n

            upper0, upper1 = self.findroot(r - 1, c)
            store0, store1 = self.findroot(r, c)
            if self.grid[store0][store1] == self.grid[upper0][upper1]:
                pass
            elif self.grid[store0][store1] < self.grid[upper0][upper1]:
                self.grid[upper0][upper1] = self.grid[store0][store1]
            else:
                self.grid[store0][store1] = self.grid[upper0][upper1]

            # print(self.grid[r][c])

            # if r == 2 :
            #    self.grid[r][c] = self.grid[0]
            #    self.grid[r-1][c] = self.grid[0]

        if c > 1 and self.grid[r][c - 1] != -1:
            # print('Case3')
            # if self.grid[r][c] == 0 :
            #    left0, left1 = self.findroot(r,c-1)
            #    self.grid[r][c] = self.grid[left0][left1]
            # else :
            # MAJOR UPDATION (not needed perhaps)
            # if r == 1 :
            #    self.grid[r][c] = -(n)

            left0, left1 = self.findroot(r, c - 1)
            store0, store1 = self.findroot(r, c)
            if self.grid[store0][store1] == self.grid[left0][left1]:
                pass
            elif self.grid[store0][store1] < self.grid[left0][left1]:
                self.grid[left0][left1] = self.grid[store0][store1]
            else:
                self.grid[store0][store1] = self.grid[left0][left1]

        if c < N - 2 and self.grid[r][c + 1] != -1:
            # print('Case4')
            # if self.grid[r][c] == 0 :
            #    right0, right1 = self.findroot(r,c+1)
            #    self.grid[r][c] = self.grid[right0][right1]

            # MAJOR UPDATION (perhaps not needed)
            # if r  == n-2 :
            #    self.grid[r][c] = n*n + 2

            right0, right1 = self.findroot(r, c + 1)
            store0, store1 = self.findroot(r, c)
            # print(right0,right1, 'Really ?')
            if self.grid[store0][store1] == self.grid[right0][right1]:
                pass
            elif self.grid[store0][store1] < self.grid[right0][right1]:
                self.grid[right0][right1] = self.grid[store0][store1]
            else:
                self.grid[store0][store1] = self.grid[right0][right1]

        if r < N - 2 and self.grid[r + 1][c] != -1:
            # print('Case2')
            # if self.grid[r][c] == 0 :
            #    lower0, lower1 = self.findroot(r+1,c)
            #    self.grid[r][c] = self.grid[lower0][lower1]

            # MAJOR UPDATION
            # if r == n-3 :
            #    self.grid[r][c] = (n-2)*(n-2) + 2

            lower0, lower1 = self.findroot(r + 1, c)
            store0, store1 = self.findroot(r, c)
            # print('Yaar.....',self.grid[store0][store1])
            # print('Yaar.....',self.grid[lower0][lower1])
            if self.grid[store0][store1] == self.grid[lower0][lower1]:
                pass
            elif self.grid[store0][store1] < self.grid[lower0][lower1]:
                self.grid[lower0][lower1] = self.grid[store0][store1]
                # if r == n-3 :
                #    self.grid[n-1] = self.grid[store0][store1]
            else:
                self.grid[store0][store1] = self.grid[lower0][lower1]
                # if r == n-3 :
                #    self.grid[n-1] = self.grid[lower0][lower1]

        # if self.grid[r][c] == 0 :
        #    self.grid[r][c] = (r-1)*5 + c

    def findroot(self, i, j):
        N = self.n
        if i < 0 or i > N - 1:
            print('Alarm for r', i)
        if j < 0 or j > N - 1:
            print('Alarm for c', j)
        if i == 0 and j > 0:
            print('In findroot, Alarm for -7 one', i, j)
        if j == N - 1 and i > 0:
            print('In findroot, Alarm for 100 one', i, j)

        exp = (N - 2) * (i - 1) + j
        # print(i,j)
        # print('This in findroot',self.grid[i][j])
        # print(n)
        try:
            while (self.grid[i][j] != exp):
                # MAJOR UPDATION
                if self.grid[i][j] == -(7):
                    return [0, 0]
                if self.grid[i][j] == 100:
                    return [N - 1, 0]

                # print('Tipi tipi top')
                # print(i,j, self.grid[i][j])
                # Steps to decompose a value back to its intended indices
                # print('Before decomposition',self.grid[i][j])
                tempi = self.grid[i][j] // (N - 2) + 1
                tempj = self.grid[i][j] % (N - 2)
                # print(tempi,tempj)
                if tempj == 0:
                    tempj = N - 2
                    tempi -= 1
                # if tempi == 0 :
                #    tempj = 0
                i = tempi
                j = tempj
                # print(i,j)
                exp = (i - 1) * (N - 2) + j
        except IndexError:
            print(i, j)
            print('Index out of range ?')
        # print(self.grid[i][j])
        # print(i,j)
        if i < 0 or i > N - 1:
            print('Alarm for r', i)
        if j < 0 or j > N - 1:
            print('Alarm for c', j)
        if i == 0 and j > 0:
            print('In findroot tail, Alarm for -7 one', i, j)
        if j == N - 1 and i > 0:
            print('In findroot tail, Alarm for 100 one', i, j)
        return [i, j]

    def isopen(self, r, c):

        if self.grid[r, c] == -1:
            return False
        return True

    def isfull(self, r, c):
        # Needs Correction
        if self.grid[r][c] == -1:
            return False

        if self.grid[r][c] == [0, 0]:
            return True
        return False

    def numberofopensites(self):
        return self.opensites

    def onesteppercolation(self):
        # MAJOR UPDATION
        N = self.n
        # print(n-1,0)
        # print(n)
        i, j = self.findroot(N - 1, 0)
        # print('Inside Percolation:', self.grid[i][j])
        if self.grid[i][j] == -7:
            return True
        return False

    def percolates(self):
        n = self.n
        # if self.grid[n-1] == self.grid[0] :
        #    return True
        # return False

        for i in range(1, self.n - 1):
            #    #print('Finally',self.grid[n-2][i])
            if self.grid[n - 2][i] == -1:
                continue
            r, c = self.findroot(n - 2, i)
            #    #print(self.grid[r][c], "root")

            if self.grid[r][c] in range(1, n - 1):
                return 'The System percolates.'
        return False

        # if self.grid[self.n - 1] == [0] :
        #    print('The System percolates.')
        #    return True
        # else :
        #    return False

    def printgrid(self):

        for i in self.grid:
            print(i)


def clientside():
    n = 5
    instance = percolation(n)
    print(instance.grid)
    instance.n = n + 2
    # openlist = [(2,3),(5,5),(3,2),(4,4),(4,3),(4,5),(5,4),(1,1),(3,5),(1,2),(2,2),(1,5),(5,1),(3,4),(3,3)]
    # (4,4),(4,3),(4,5),(5,4),(1,1),(3,5),(1,2),(2,2)(1,5),(5,1),(3,4),(3,3)]
    # for cells in openlist :
    #    instance.open(cells[0], cells[1])

    print('\n')
    # print(instance.isfull(3,2)

    import random
    check = instance.onesteppercolation()
    while check == False:
        #    print('Input................')
        r = random.randint(1, n)
        c = random.randint(1, n)
        instance.open(r, c)
        check = instance.onesteppercolation()
    print(instance.onesteppercolation())
    print('Number of open sites in the grid:', instance.numberofopensites())
    print(instance.printgrid())


# clientside()
import statistics


class PercolationSimulation():

    # perform independent trials on an n-by-n grid.
    def __init__(self, n, trials):
        self.t = trials
        i = 0
        self.thresholds = []
        import random

        while i < trials:
            # print('#')

            instance = percolation(n)
            # print(instance.grid)
            instance.n = n + 2
            check = instance.onesteppercolation()

            while check == False:
                r = random.randint(1, n)
                c = random.randint(1, n)
                instance.open(r, c)
                check = instance.onesteppercolation()

            opensites = instance.numberofopensites()
            # print(opensites)
            self.thresholdvalue = opensites / (n * n)
            # print(self.thresholdvalue)
            self.thresholds.append(self.thresholdvalue)
            i += 1

    def meanvalue(self):
        self.avg = statistics.mean(self.thresholds)
        print('Mean:', self.avg)
        print(self.thresholds)

    def stddev(self):
        self.stddev = statistics.stdev(self.thresholds)
        print('Standard Deviation:', self.stddev)

    def lowbound(self):
        self.low = self.avg - (1.96 * self.stddev) / self.t
        print('Low Bound for 95% Confidence Interval', self.low)

    def highbound(self):
        self.high = self.avg + (1.96 * self.stddev) / self.t
        print('High Bound for 95% Confidence Interval', self.high)


def UserInterface():
    print('Hi, I hope you\'re ready for running the simulations pertaining to the Percolation problem.\nPress any key to begin.')
    key = input()
    n = int(input('\nEnter the Grid size(n): '))
    t = int(input('\nEnter the number of trials required: '))
    simulator = PercolationSimulation(n, t)
    simulator.meanvalue()
    simulator.stddev()
    simulator.lowbound()
    simulator.highbound()


UserInterface()

