class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes_list = list(dominoes)
        n = len(dominoes_list)
        forces = [0] * n
        force = 0
        for i in range(n):
            if dominoes_list[i] == "R":
                force = n
            elif dominoes_list[i] == "L":
                force = 0
            else:
                force = max(force - 1, 0)
            forces[i] += force

        for i in range(n-1, -1, -1):
            if dominoes_list[i] == "L":
                force = n
            elif dominoes_list[i] == "R":
                force = 0
            else:
                force = max(force - 1, 0)
            forces[i] -= force

        result = []
        for i in range(len(forces)):
            if forces[i] > 0:
                result.append("R")
            elif forces[i] < 0:
                result.append("L")
            else:
                result.append(".")
        return "".join(result)

        
