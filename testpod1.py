#! /usr/bin/python
from appy.pod.renderer import Renderer

class Campo2:
    id=0
    valore=''
    def __init__(self,id=None,val=None):
        self.id=id
        self.valore=val


campo1='questo campo viene assegnato nello script python!!! '
lista = []
lista.append(Campo2(1,'pippo'))
lista.append(Campo2(2,'pluto'))

# create a ODT report
renderer = Renderer('testpod1.odt',globals(), 'result.odt')
renderer.run()

# create a PDF report
renderer = Renderer('testpod1.odt',globals(), 'result.pdf',pythonWithUnoPath='/opt/libreoffice5.0/program/python')
renderer.run()

