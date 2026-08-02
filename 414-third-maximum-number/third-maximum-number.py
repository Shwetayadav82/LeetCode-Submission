class Solution(object):
    def thirdMax(self, nums):
        # Remove duplicates kre gae set ke help se sirf unique value aata h 
        nums = list(set(nums))

        # Sort kre gae  descending order mae ku ki humko 3rd value niklna h 
        nums = sorted(nums, reverse=True)

        # agar value 3 number se bada ho ga toh else part print ho ga matlab 0 index wala value agar chota ho ga toh 3rd index ka value print hp ga 
        if len(nums) >= 3:
            return nums[2]
        else:
            return nums[0]