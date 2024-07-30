func containsDuplicate(nums []int) bool {

    dic := make(map[int]bool)

    for _,num := range(nums){
        if dic[num] == true{
            return true
        }else{
            dic[num] = true

            
        }
    }
    
    return false
    
}