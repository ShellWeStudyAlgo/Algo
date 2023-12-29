# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        print(l1) # ListNode{val: 2, next: ListNode{val: 4, next: ListNode{val: 3, next: None}}}

        result = ""
        result2 = ""      
        #current_node = l1
        #while current_node:
            #print(current_node.val)
            #result += str(current_node.val) + ""
            #current_node = current_node.next
            #print(result)
        
        
        while l1 and l2:
            result += str(l1.val) + ""
            l1 = l1.next
            result2 += str(l2.val) + ""
            l2 = l2.next
            print(result,result2) #여기까지 출력값 243 564
                    
        answer = int(result) + int(result2) #여기까지 807
        print(answer)

        #순서 역전하기
        #한자리씩 끊어서 다시 리스트에 넣기


            
        