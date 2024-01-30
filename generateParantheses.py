
input = 4
curr_str = []
valid_op = []

def generateParantheses(frwd_paran:int, bkwd_paran:int) -> None:

    if frwd_paran == 0 and bkwd_paran == 0:
        valid_op.append("".join(curr_str))

    if frwd_paran > 0:
        curr_str.append("(")
        generateParantheses(frwd_paran-1,bkwd_paran)

    if bkwd_paran > 0 and frwd_paran < bkwd_paran:
        curr_str.append(")")
        generateParantheses(frwd_paran,bkwd_paran-1)

    if len(curr_str) > 0:
        curr_str.pop()

generateParantheses(input,input)
print("valid_op: ",valid_op)

