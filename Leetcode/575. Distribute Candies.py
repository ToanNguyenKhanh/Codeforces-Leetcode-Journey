def distributeCandies(candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        x = int(len(candyType) / 2)
        candy_set = set(candyType)
        if len(candy_set)>x:
            return x
        return len(candy_set)

if __name__ == '__main__':
    candyType = [1, 1, 2, 2, 3, 3]
    print(distributeCandies(candyType))


