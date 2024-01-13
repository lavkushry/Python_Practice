# Problem is
# For given string S and integers P and Q, which denotes the cost of removal of substrings “he” and “lo” respectively from S, the task is to find the maximum cost of removing all occurrences of substrings “he” and “lo”.
# example if S = “hellohellohellohellohello”, P = 6, Q = 4, then cost to remove 'he' and 'lo' is 50

S = "hellohellohellohellohello"

# Costs
P = 6;
Q = 4;


def MaxCollection(S, P, Q):
    maxstr = [i for i in ("he" if P >= Q else "lo")]
    minstr = [i for i in ("lo" if P >= Q else "he")]
    maxp = max(P, Q)
    minp = min(P, Q)
    cost = 0
    stack1 = []
    s = [i for i in S]
    for ch in s:
        if (len(stack1)> 0 and (stack1[-1]== maxstr[0] and ch == maxstr[1])):
            del stack1[-1]
            cost +=maxp
        else:
            stack1.append(ch)
    sb=""
    while (len(stack1)>0):
        sb += stack1[-1]
        del stack1[-1]

    sb=sb[::-1]
    remstr=sb
    for ch in remstr:
        if (len(stack1)>0 and (stack1[-1]==minstr[0] and ch == minstr[1])):
            del stack1[-1]
            cost +=minp
        else:
            stack1.append(ch)

    return cost

if __name__ == "__main__":
    S = "hellohellohellohellohello"

    # Costs
    P = 6;
    Q = 4;

print(MaxCollection(S, P, Q));