class HuffmanCode():

    class Node():

        def __init__(self, left, right):
            self.left = left
            self.right = right
            self.freq = None

    def __init__(self, array):

        def findMin(Q):
            length = len(Q)
            min = None
            q_list = list(Q)
            for i in range(length-1):
                if (q_list[i].freq or q_list[i] < q_list[i+1].freq or q_list[i+1]):
                    q_list[i], q_list[i+1] = q_list[i+1], q_list[i]
            return q_list[-1]

        Q = set(array)
        length = len(Q)
        for i in (length-1):
            z = self.Node()
            z.left = x = Q.pop(findMin(Q))
            z.right = y = Q.pop(findMin(Q))
            z.freq = (x.freq or x) + (y.freq or y)
            Q.add(z)
        return findMin(Q)



