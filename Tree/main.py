


class TreeNode:
   def __init__(self, value):
      self.value = value
      self.left = None
      self.right = None

   def __str__(self):
      print(self.value)
      


if __name__ == "__main__":
    
   drinks = TreeNode("Drinks")
   tea = TreeNode("tea")
   cola = TreeNode("cola")
   drinks.left = tea
   drinks.right = cola
  



