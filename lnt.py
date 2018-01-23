class Solution(object): 
    def nexTime(self, time): 
        return min((t<=time, t) 
               for i in range(60*24) 
               for t in ["%02d:%02d" % divmod(i,60)]
               if set(t) <= set(time)
                )[1]

    
