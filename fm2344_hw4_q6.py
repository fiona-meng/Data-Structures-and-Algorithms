def appearances(s, low, high):
    if low == high:
        return {s[low] : 1}
    else:
        result = appearances(s, low + 1, high)
        if s[low] in appearances(s, low + 1, high):
            result[s[low]] += 1
        else:
            result[s[low]] = 1
        return result



print(appearances("Hello world", 0, 10))
