class Solution:
    def solve(self, matrix):
        dependents = defaultdict(set)
        dependencies = defaultdict(set)
        stack = []

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c][0].isalpha():
                    r2 = int(matrix[r][c][1:])-1
                    c2 = ascii_uppercase.index(matrix[r][c][0])
                    dependents[(r2,c2)].add((r,c))
                    dependencies[(r,c)].add((r2,c2))
                elif matrix[r][c][0] == "=":
                    split_char = "+" if "+" in matrix[r][c] else "-"
                    args = matrix[r][c][1:].split(split_char)

                    for arg in args:
                        if arg[0].isalpha():
                            r2 = int(arg[1:])-1
                            c2 = ascii_uppercase.index(arg[0])
                            dependents[(r2,c2)].add((r,c))
                            dependencies[(r,c)].add((r2,c2))

                    if not dependencies[(r,c)]: stack.append((r,c))
                else:
                    matrix[r][c] = matrix[r][c]
                    stack.append((r,c))

        while stack:
            r,c = stack.pop()

            if matrix[r][c][0].isalpha():
                r2 = int(matrix[r][c][1:])-1
                c2 = ascii_uppercase.index(matrix[r][c][0])
                matrix[r][c] = matrix[r2][c2]
            elif matrix[r][c][0] == "=":
                split_char = "+" if "+" in matrix[r][c] else "-"
                args = matrix[r][c][1:].split(split_char)
                final_args = []

                for arg in args:
                    if arg[0].isalpha():
                        r2 = int(arg[1:])-1
                        c2 = ascii_uppercase.index(arg[0])
                        final_args.append(str(matrix[r2][c2]))
                    else:
                        final_args.append(arg)

                matrix[r][c] = eval(split_char.join(final_args))
            else:
                matrix[r][c] = int(matrix[r][c])

            for r2,c2 in dependents[(r,c)]:
                dependencies[(r2,c2)].remove((r,c))
                if not dependencies[(r2,c2)]: stack.append((r2,c2))

        return [list(map(str, row)) for row in matrix]
