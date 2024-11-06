
class Visitor(object):
    def visit(self,obj:'Visitable'):
        pass
    
class Visitable(object):
    def accept(self,visitor:Visitor,callback:callable[...,None]|None):
        visitor.visit(self)