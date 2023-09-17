class Candies:
    def candies_distribution(self,n,arr):
        candy = [1]*n
        for i in range(1,n):
            if arr[i]>arr[i-1]:
                candy[i] = candy[i-1]+1
        for i in range(n-2,-1,-1):
            if arr[i]>arr[i-1]:
                candy[i] = max(candy[i],candy[i-1]+1)
        return sum(candy)
    
Candies_obj = Candies()
arr=[2,4,2,6,1,7,8,9,2,1]
print(Candies_obj.candies_distribution(10,arr))
            
            