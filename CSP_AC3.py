import queue
ROW = "ABCDEFGHI"
COL = "123456789"

class CSP:
    def __init__(self, board):
        self.variables = [k for k in board.keys()]
        self.mapping = board
        self.domain = self.get_domain(board)
        self.combinations = ([[r+c for r in ROW] for c in COL] + [[r+c for c in COL] for r in ROW] + [[r+c for r in r_grid for c in c_grid] for r_grid in ('ABC','DEF','GHI') for c_grid in ('123','456','789')])
        self.comb_dicts = dict((key, [c for c in self.combinations if key in c]) for key in self.variables)
        self.neighbors = dict((key, set(sum(self.comb_dicts[key],[]))-set([key])) for key in self.variables)
        self.constraints = {(var, n) for var in self.variables for n in self.neighbors[var]}
    def get_domain(self, board):
        domain = {}
        for key, values in self.mapping.items():
            if values == 0:
                domain[key] = [1,2,3,4,5,6,7,8,9]
            else:
                domain[key] = [values]
        return domain
    

def AC3(csp):
    q = queue.Queue()
    for each_arc in csp.constraints:
        q.put(each_arc)
    while not q.empty():
        (Xi, Xj) = q.get()
        if Revise(csp, Xi, Xj):
            if len(csp.domain[Xi]) == 0:
                return 0
            for Xk in (csp.neighbors[Xi] - set(Xj)):
                q.put((Xk, Xi))
    return 1
def Revise(csp, Xi, Xj):
    revised = 0
    for x in set(csp.domain[Xi]):
        if not is_Consistent(csp, x, Xi, Xj):
            csp.domain[Xi].remove(x)
            revised = 1 
    return revised 

def is_Consistent(csp, x, Xi, Xj):
    for y in csp.domain[Xj]:
        if Xj in csp.neighbors[Xi] and y!=x:
            return 1
    return 0