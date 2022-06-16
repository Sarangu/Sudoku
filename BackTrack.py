from copy import deepcopy
failure = "FAILURE"

def BackTrack(assignment, csp):
    if set(assignment.keys())==set(csp.variables):
        return assignment
    var = Select_Unassigned_Variables(assignment, csp)
    domain = deepcopy(csp.domain)
    for value in Order_Domain_Values(var, assignment, csp):
        if is__Consistent(var, value, assignment, csp):
            assignment[var] = value
            inferences = {}
            inferences = Inference(assignment, inferences, csp, var, value)
            if inferences!= failure:
                result = BackTrack(assignment, csp)
                if result!= failure:
                    return result
            del assignment[var]
            csp.domain.update(domain)
    return failure

def is__Consistent(var, value, assignment, csp):
    for neighbor in csp.neighbors[var]:
        if neighbor in assignment.keys() and assignment[neighbor]==value:
            return 0
    return 1

def Select_Unassigned_Variables(assignment, csp):
    unassigned_vars = dict((var, len(csp.domain[var])) for var in csp.domain if var not in assignment.keys())
    res = min(unassigned_vars, key=unassigned_vars.get)
    return res


def Order_Domain_Values(var, assignment, csp):
    return csp.domain[var]

def Inference(assignment, inferences, csp, var, value):
    inferences[var] = value
    for neighbor in csp.neighbors[var]:
        if neighbor not in assignment and value in csp.domain[neighbor]:
            if len(csp.domain[neighbor])==1:
                return failure
            csp.domain[neighbor].remove(value)
            rem = csp.domain[neighbor]
            if len(rem) == 1:
                if Inference(assignment, inferences, csp, neighbor, rem) == failure:
                    return failure
    return inferences