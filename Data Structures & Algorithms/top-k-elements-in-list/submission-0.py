class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        pairs = [[] for i in range(len(nums) + 1)]


        for num in nums:
            mp[num] = mp.get(num,0) + 1

        for num, cnt in mp.items():
            pairs[cnt].append(num)  

        res = [] 
        for i in range(len(pairs) - 1, 0, -1):
            for num in pairs[i]:
                res.append(num)
                if len(res) == k:
                    return res
        
            



        


        


        

        