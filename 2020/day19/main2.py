
file = open("input.txt")

nodeId = -1
def nodeId():
    global nodeId
    nodeId -= 1
    return nodeId

def orNode():
    return {
        "type": "or",
        "children": []
    }

def andNode():
    return {
        "type": "and",
        "children": []
    }

def finalNode(val):
    return {
        "type": "final",
        "val": val
    }

def ruleNode(ruleId):
    return {
        "type": "rule",
        "child": None,
        "ruleId": ruleId
    }

input = file.read().split("\n\n")
input = [m.split("\n") for m in input]
rules = {}
for rule in input[0]:
    r = rule.split(": ")
    if "\"" in r[1]:
        rules[r[0]] = r[1].replace("\"", "")
    else:
        a = r[1].split(" | ")
        rules[r[0]] = [b.split(" ") for b in a]


rules["8"] = [["42"], ["42", "8"]]
rules["11"] = [["42", "31"], ["42", "11", "31"]]
messages = input[1]

g = {}
visited = {}
for ruleId, rule in rules.items():
    g[ruleId] = ruleNode(ruleId)
    visited[ruleId] = 0

for ruleId, rule in rules.items():
    if type(rule) == str:
        fNode = finalNode(rule)
        g[ruleId]["child"] = fNode
    else:
        oNode = orNode()
        g[ruleId]["child"] = oNode
        for r in rule:
            aNode = andNode()
            oNode["children"].append(aNode)
            for v in r:
                aNode["children"].append(g[v])

def printGraph(u=g["0"], path=""):
    if u["type"] == "final":
        path = path + " -> final {}".format(u["val"])
        print(path)
        return

    if u["type"] == "or" or u["type"] == "and":
        path = path + " -> " + u["type"]
        for c in u["children"]:
            printGraph(c, path)
    elif u["type"] == "rule":
        path = path + " -> rule {}".format(u["ruleId"])
        printGraph(u["child"], path)

state = None
flag = False
def f(chk, u, loop_max):
    global state
    global visited
    global flag
    #print(chk + "  " + state)

    if u["type"] == "final":
        #print(state + " + " + u["val"], "Expected " + chk[len(state)])
        if chk[len(state)] == u["val"]:
            state += u["val"]
            if len(state) == len(chk):
                print("FLAG")
                flag = True
            return True
        else:
            return False  # Backtrack
    elif u["type"] == "rule":
        if flag:
            return False
        #print(str(visited[u["ruleId"]])  + " / " + str(loop_max))
        if visited[u["ruleId"]] == loop_max:
            return True
        visited[u["ruleId"]] += 1
        #print("Rule {}".format(u["ruleId"]))
        return f(chk, u["child"], loop_max)
    elif u["type"] == "and":
        # Count loops
        visited_copy = visited.copy()
        original_state = state[:]
        loopsId = []
        for c in u["children"]:
            if visited[c["ruleId"]] > 0:
                loopsId.append(c["ruleId"])
        loopsControl = [[0 for i in range(len(loopsId))]]
        while True:
            l = list(loopsControl[-1])
            for i in range(len(l)):
                if l[i] == 0:
                    l[i] = 1
                    break
                else:
                    l[i] = 0
            loopsControl.append(l)
            if len(loopsControl) >= 2 ** len(loopsId):
                break
        ret = False
        for control in loopsControl:
            loopId = 0
            visited = visited_copy.copy()
            state = original_state[:]
            for c in u["children"]:
                if c["ruleId"] in loopsId:
                    if control[loopId] == 1:
                       if not f(chk, c, loop_max):
                           break
                    else:
                        continue
                    loopId += 1
                else:
                    if not f(chk, c, loop_max):
                        break
                if flag:
                    return False
            if flag:
                return False
            ret = True
        return ret
    elif u["type"] == "or":
        visited_copy = visited.copy()
        original_state = state[:]
        ret = False
        for c in u["children"]:
            visited = visited_copy.copy()
            state = original_state[:]
            ret = ret or f(chk, c, loop_max)
            if flag:
                return False

        return ret

count = 0
visited_original = visited.copy()
for id, msg in enumerate(messages):
    print("{}/{}".format(id, len(messages)))
    for loop_max in range(1, len(msg)):
        flag = False
        state = ""
        visited = visited_original.copy()
        ret = f(msg, g["0"], loop_max)
        if flag:
            print("We got it")
            count += 1
            break
print(count)
