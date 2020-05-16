# English Ruler implementation using recursion.
def draw_line(nums, label=''):          # --- 0
    line = '-' *nums
    if label:
        line += ' ' + label
    print(line)                         #           --
                                        #           -
def intervals(interval_nums):# Rcursion Func 3      ---
    if interval_nums > 0:               #           -
        intervals((interval_nums-1))    #           --
        print('-' * interval_nums)
        intervals((interval_nums-1))
# Drawing the Ruler using the up both functions
def ruler(inches,minuses):
    draw_line(minuses,'0')             # first line ---0
    for i in range(1, 1+inches):
        intervals(inches-1)            # draw interior ticks for inch
        draw_line(minuses, str(i))      # draw inch i line and label

ruler(3,3)
