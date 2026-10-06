class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        uniqueKeyList = list(set(nums))
        # print(f"uniqueKeyList: {uniqueKeyList}")
        counterDict = {num: 0 for num in uniqueKeyList}
        # print(f'counterDict: {counterDict}')
        for num in nums:
            counterDict[num]=counterDict.get(num)+1

        # print(f'counterDict: {counterDict}')
        sortedDict = {num: count for num,count in sorted(counterDict.items(),key=lambda item: item[1],reverse=True)}
        # print(f'sortedDict: {sortedDict}')
        counter = 0
        resultList = []
        for key,v in sortedDict.items():
            if counter<k:
                counter+=1
                resultList.append(key)
            
        return resultList