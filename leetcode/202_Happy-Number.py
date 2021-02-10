class Solution:
    def isHappy(self, n: int) -> bool:
        def square_sum(ns):
            s = 0
            for n in ns:
                s += n*n
            return s

        def parse(n):
            ns = [n%10]
            n //= 10
            while n:
                ns.append(n%10)
                n //= 10
            return tuple(ns)
        
        ns_set = set()
        ns = parse(n)
        ns_set.add(ns)
        ss = square_sum(ns)
        while ss != 1:
            ns = parse(ss)
            if ns in ns_set:
                return False
            ns_set.add(ns)
            ss = square_sum(ns)

        return True

s = Solution()
print(s.isHappy(1111111))