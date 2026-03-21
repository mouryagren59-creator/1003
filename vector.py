class vector():
    def __init__(self, components):
        self.components = components

    def __str__(self):
        return f"vector ({self.components})"
    
    def __len__(self):
        return len(self.components)
    
    def scalar_multiply(self, scalar):
        return vector([scalar ( x for x in self.components)])