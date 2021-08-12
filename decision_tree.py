from anytree import NodeMixin, RenderTree
import tkinter
class WNode(NodeMixin):

   def __init__(self, name, parent=None, weight=None):
       super(WNode, self).__init__()
       self.name = name
       self.parent = parent
       self.weight = weight if parent is not None else None

   def _post_detach(self, parent):
      self.weight = None

