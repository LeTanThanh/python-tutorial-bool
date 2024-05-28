class Person:
  def __init__(self, first_name, last_name, age) -> None:
    self.first_name = first_name
    self.last_name = last_name
    self.age = age

  def __bool__(self) -> bool:
    if self.age < 18 or self.age > 65:
      return False

    return True
