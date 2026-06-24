def display(s,ind):
    if ind ==len(s):
        return
    print(s[:ind+1])
    display(s,ind+1)
display ("python",0)
