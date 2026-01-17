class Node:
    def __init__(self, x = None, y = None):
        self.x    = x
        self.y    = y
        self.prev = None
        self.next = None

    def __str__(self) -> str:
        return str(f"x:{self.x}, y:{self.y}")

    def __repr__(self) -> str:
        return self.__str__()

class DoublyLinkedList:
  def __init__(self):
      self.header = Node()   # sentinel node at the beginning
      self.tailer = Node()   # sentinel node at the end
      self.header.next = self.tailer
      self.tailer.prev = self.header
      self.size = 0

  def __str__(self) -> str:
      value_str = "["
      if self.size == 0:
        return None
      else:
        current = self.header.next
        while current != self.tailer:
          value_str += str(current) + " "
          current = current.next
        value_str += "]"
      return value_str
  
  def add_first(self, value):
    """
  Adds a node to the beginning of the list
  parameters:  value
                value of the node
  returns
      None
  """
    # print("adding first: ", value)
    newNode = Node(value)
    self.header.next.prev = newNode
    newNode.next          = self.header.next
    self.header.next      = newNode
    newNode.prev          = self.header
    self.size += 1

  def add_last(self, x, y):
    """
  Adds a node to the end of the list
  parameters:  
              x : 
                x value of the node
              y:
                y value of the node

  returns
      None
  """
    #print("adding last: ", x, y)
    newNode = Node(x, y)
    self.tailer.prev.next = newNode
    newNode.prev          = self.tailer.prev
    self.tailer.prev      = newNode
    newNode.next          = self.tailer   
    self.size += 1

  def first(self):
    """
  Returns the value of the first node in the linked list
  parameters:  None
  returns
      None
  """
    return self.header.next
  
  def last(self):
    """
  Returns the value of the last node in the linked list
  parameters:  None
  returns
      None
  """
    return self.tailer.prev

  def get(self, i: int):
    """
  Returns the value of a node at index i
  parameters:  i : int
                value from 0 to n-1 nodes
  returns
      value of the deleted node, or value error if invalid entry
  """
    current = self.header.next
    if i < 0 or i > self.size - 1:
      raise ValueError("Index value must be less than list size and be non-negative")
    
    
    elif i == 0:
      x = current.x
      y = current.y

      return (x, y)
  
    while i != 0:
      i = i - 1
      current = current.next

    x = current.x
    y = current.y

    return (x, y)
      
  def get_size(self)->int:
    """
  Returns the value of the first node in the linked list
  parameters:  None
  returns
      integer size of the linked list
  """
    return self.size
  
  def is_empty(self)->bool:
    """
  Determines if the list is empty
  parameters:  None
  returns
      bool, True if the list is empty
  """
    return self.size == 0


  def remove_first(self):
    """
      Removes the first node of a DoublyLinkedList
      
      parameters: none
      returns
          value of the deleted node
    """
    return self.remove_between(self.header, self.header.next.next)
      
  def remove_last(self):
    """
      Removes the last node of a DoublyLinkedList
      
      parameters: none
      returns
          value of the deleted node
    """
    return self.remove_between(self.tailer.prev.prev, self.tailer)
  
 
  


def main():
  pass


if __name__ =="__main__":
  main()