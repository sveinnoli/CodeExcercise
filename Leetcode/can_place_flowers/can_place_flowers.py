class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        cursor=0
        places=0
        while cursor < len(flowerbed)-1:
            if (flowerbed[cursor]):
                cursor += 2
                continue
            else:
                if (not flowerbed[cursor+1]):
                    flowerbed[cursor] = 1
                    places += 1
                    cursor += 2
                    continue
                cursor += 1
        if (len(flowerbed) > 1):
            if not flowerbed[-1] and not flowerbed[-2]:
                places += 1
        else:
            if not flowerbed[0]:
                places += 1
        return places >= n
    
        if (2 in array):

if __name__ == "__main__":
    s=Solution()
    r=s.canPlaceFlowers([1,0,0,0,1], 1)
    print(r)