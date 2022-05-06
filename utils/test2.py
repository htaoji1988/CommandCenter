res = []


def dfs(wait, stack, out):
    if not wait and not stack:
        res.append(' '.join(map(str, out)))
    if wait:
        dfs(wait[1:], stack + [wait[0]], out)
    if stack:
        dfs(wait, stack[:-1], out + [stack[-1]])


while True:
    try:
        n = int(input())
        trains = list(map(int, input().split()))
        dfs(trains, [], [])
        for i in sorted(res):
            print(i)
    except:
        break
