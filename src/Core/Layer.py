class Layer:
    def __init__(self, name: str):
        self.m_Name = name

    def OnAttach(self):
        """Called when the layer is attached to the stack."""
        print(f"Layer {self.name} attached.")

    def OnDetach(self):
        """Called when the layer is detached from the stack."""
        print(f"Layer {self.name} detached.")

    def OnUpdate(self):
        """Update the layer."""
        print(f"Updating layer {self.name}.")

    def OnRender(self):
        """Render the layer."""
        print(f"Rendering layer {self.name}.")
