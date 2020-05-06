'''''Remove Linked List Elements: Remove all elements from a linked list that contain a given value.'''


# (1)->(2)->(3)->(4) (2)

# if we remove the point of the value node it deletes the node
# LOOP through the list find value
# once value match assign the current value to next node


# on = self.head
# value = self.value

# for on in linked list
# if on == value:
# on.next == on.next.next
# on.next == on


def delete_by_value(self, value):
    # pointer
    on = self
    # checking for on and on.next for deletion
    while on and on.next:
        # if it doesnt match keep chaning pointers until found value
        if on.next.value == value:
            on.next = on.next.next
    # reassign next node to current node
        on = on.next


""" Time complexity is 0(n) because it has to loop through each node to find value: linear time"""
