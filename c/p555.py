import sys

def mac(m, k, s, n):
    if n > m:
        return n - s
    else:
        return mac(m, k, s, mac(m, k, s, n + k))


def highest_fp(m, k, s):
    return m - 2 * s + k


def fmac(m, k, s):
    # FIXED POINT PATTERN:
    # e.g. (100, 68, 64) , [37, 38, 39, 40]
    # def f(m, k, s):
    #     return m - 2*s + k
    # This function returns the largest fixed point
    # The rest are the consecutive numbers descending from this
    # The number of fixed points equals k - s
    num_points = k - s
    if s % num_points != 0:
        return []

    highest = highest_fp(m, k, s)
    lowest = highest - (k - s) + 1
    fixed_points =  range(lowest, highest + 1)
    # print (m, k, s), ',', fixed_points
    return fixed_points
    # for i in range(m + k):
    #     if i == mac(m, k, s, i):
    #         fixed_points.append(i)

    # if fixed_points:
    #     print (m,k,s), ',', fixed_points
    # return fixed_points


def sf(m, k, s):
   return sum(fmac(m, k, s))


def s(p, m):
    return sum([sf(m, k, s) for s in range(1, p + 1) for k in range(s + 1, p + 1)])


if __name__ == '__main__':
    try:
        p, m = sys.argv[1:3]
    except:
        print "Args required: p, m"
        sys.exit(1)

    print s(int(p), int(m))
