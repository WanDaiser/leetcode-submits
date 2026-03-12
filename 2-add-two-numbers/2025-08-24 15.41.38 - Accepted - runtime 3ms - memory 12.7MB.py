# Linked list'i listeye çevir
def linked_list_to_list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res

# Listeyi tekrar linked list'e çevir
def list_to_linked_list(lst):
    dummy = ListNode(0)
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        # Linked list -> liste
        def linked_list_to_list(node):
            res = []
            while node:
                res.append(node.val)
                node = node.next
            return res

        # Liste -> linked list
        def list_to_linked_list(lst):
            dummy = ListNode(0)
            current = dummy
            for val in lst:
                current.next = ListNode(val)
                current = current.next
            return dummy.next

        l1_list = linked_list_to_list(l1)
        l2_list = linked_list_to_list(l2)

        max_len = max(len(l1_list), len(l2_list))
        while len(l1_list) < max_len:
            l1_list.append(0)
        while len(l2_list) < max_len:
            l2_list.append(0)

        l3 = []
        carry = 0
        for i in range(max_len):
            tempres = l1_list[i] + l2_list[i] + carry
            carry = tempres // 10
            l3.append(tempres % 10)

        # Eğer sonrasında carry kaldıysa ekle
        if carry > 0:
            l3.append(carry)

        return list_to_linked_list(l3)
