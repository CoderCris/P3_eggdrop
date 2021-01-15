def solve_memoization(eggs_num, floors):
    memo = {}

    def aux_memoization(eggs, floors):

        if eggs == 1 or floors < 2:
            memo[eggs, floors] = floors
            return floors
        if memo.get((eggs, floors)) is not None:
            return memo[eggs, floors]
        else:
            #minimo = sys.maxsize
            memo[eggs, floors] = min(
                1 + max(aux_memoization(eggs - 1, x - 1), aux_memoization(eggs, floors - x)) for x in
                range(1, floors+1))

        return memo[eggs, floors]

    aux_memoization(eggs_num, floors)
    return memo