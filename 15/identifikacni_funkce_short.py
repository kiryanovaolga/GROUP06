class Example:
    def __init__(self):
        self.name = "Test"
        self.value = 42

    def method(self):
        return "Hello, world!"

# Create an object
obj = Example()

# Built-in methods
print("dir():", dir(obj))                  # List attributes and methods
print("vars():", vars(obj))                # Dictionary of attributes
print("type():", type(obj))                # Type of the object
print("id():", id(obj))                    # Memory address of the object
print("isinstance():", isinstance(obj, Example))  # Check object type
print("hasattr():", hasattr(obj, 'name'))  # Check if 'name' exists
print("getattr():", getattr(obj, 'name'))  # Get value of 'name'
setattr(obj, 'name', "New Name")           # Set value of 'name'
print("setattr():", obj.name)              # Updated name
delattr(obj, 'value')                      # Delete 'value'
print("delattr():", hasattr(obj, 'value')) # Check if 'value' exists