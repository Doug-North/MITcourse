s = 'zyxba'

first_index = 0     # Length of strings once a < b (transient) returns to 0 if not true
holding = 0         # Length of longest string
index_of_s = 0      # index of s
end_posit = 0
s += ' '
for letter in range(len(s)-1):
    if s[letter] <= s[letter+1]:
        first_index += 1
        index_of_s += 1
    elif s[letter] > s[letter+1]:
        if first_index > holding:
            holding = first_index
            index_of_s += 1
            end_posit = index_of_s+1
            first_index = 0
        else:
            first_index = 0
            index_of_s += 1
    first_posit = (end_posit-1) - (holding+1)

print('longest substring in alphabetical order is:', s[first_posit:end_posit-1])
