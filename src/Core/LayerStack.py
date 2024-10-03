from Layer import Layer

class LayerStack:
    def __init__(self):
        self.m_Layers = []  # List to hold layers
        self.m_LayerInsertIndex = 0

    def PushLayer(self, layer: Layer):
        """Push a layer onto the stack."""
        self.m_Layers.insert(self.m_LayerInsertIndex, layer)
        layer.OnAttach()  # Call OnAttach for the layer
        self.m_LayerInsertIndex += 1

    def PushOverlay(self, overlay: Layer):
        """Push an overlay layer onto the stack."""
        self.m_Layers.append(overlay)
        overlay.OnAttach()  # Call OnAttach for the overlay

    def PopLayer(self, layer: Layer):
        """Pop a layer from the stack."""
        if layer in self.m_Layers:
            layer.OnDetach()  # Call OnDetach for the layer
            self.m_Layers.remove(layer)
            self.m_LayerInsertIndex -= 1

    def PopOverlay(self, overlay: Layer):
        """Pop an overlay layer from the stack."""
        if overlay in self.m_Layers:
            overlay.OnDetach()  # Call OnDetach for the overlay
            self.m_Layers.remove(overlay)

    def __getitem__(self, index: int) -> Layer:
        """Get a layer by index with boundary checking."""
        if index < 0 or index >= len(self.m_Layers):
            raise IndexError("Layer index out of range.")
        return self.m_Layers[index]

    def Size(self) -> int:
        """Return the number of layers in the stack."""
        return len(self.m_Layers)

    def __iter__(self):
        """Iterator for the LayerStack."""
        return iter(self.m_Layers)

    def __len__(self):
        """Return the number of layers for len() support."""
        return len(self.m_Layers)
