from src.patterns.visitor import Visitable

class Node(Visitable):
    
    def __init__(self,node_id=None) -> None:
        self.node_id=node_id
        self.parent:Node=None
        self.children:set[Node]=set()
    
    def addChild(self,child:'Node'|any|None=None):
        child_type=type(child)
        if child_type!=Node:
            child=Node(child)
        child.parent=self
        self.children.add(child)
        
    def removeChild(self,child:'Node'|any)->'Node':
        child_type=type(child)
        if child_type!=Node:
            child=Node(child)
        child.parent=None
        self.children.discard(child)
        return child

    def __repr__(self) -> str:
        return f"Node_id: {self.node_id}\nParent: {self.parent.node_id}\nChildren: {','.join([child.node_id for child in self.children])}"
    
    