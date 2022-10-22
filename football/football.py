budget = int(input())
class Person:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

def read_n_persons(n):
    res = []
    for _ in range(n):
        name, salary = input().split("")
        res.append(Person(name=name, salary=int(salary)))
    return res

point_guards = read_n_persons(int(input()))
shooting_guards = read_n_persons(int(input()))
small_fordwares = read_n_persons(int(input()))
fordwares = read_n_persons(int(input()))
centrals = read_n_persons(int(input()))

class Solution:
    def __int__(self, point_guard, shooting_guard, small_fordware, fordware, central):
        self.point_guard: Person = point_guard
        self.shooting_guard: Person = shooting_guard
        self.small_fordware: Person = small_fordware
        self.fordware: Person = fordware
        self.central: Person = central

    def get_value(self):
        return 0 + self.point_guard.salary + self.shooting_guard.salary \
               + self.small_fordware.salary + self.fordware.salary + self.central.salary

# Seems like a backpack problem, witch should probably be solved with dynamic programming

def totalvalue(sol: Solution):
    ' Totalise a particular combination of items'
    value = sol.get_value()
    return (value, value)

def knapsack(items, limit):
    table = [[0 for w in range(limit + 1)] for j in range(len(items) + 1)]

    for j in range(1, len(items) + 1):
        item, wt, val = items[j-1]
        for w in range(1, limit + 1):
            if wt > w:
                table[j][w] = table[j-1][w]
            else:
                table[j][w] = max(table[j-1][w],
                                  table[j-1][w-wt] + val)

    result = []
    w = limit
    for j in range(len(items), 0, -1):
        was_added = table[j][w] != table[j-1][w]

        if was_added:
            item, wt, val = items[j-1]
            result.append(items[j-1])
            w -= wt

    return result


bagged = knapsack01_dp(items, 400)
print("Bagged the following items\n  " +
      '\n  '.join(sorted(item for item,_,_ in bagged)))
val, wt = totalvalue(bagged)
print("for a total value of %i and a total weight of %i" % (val, -wt))
