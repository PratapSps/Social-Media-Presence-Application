'''
Created on Jun 3, 2017

@author: Survya Pratap
'''
from sps.GUI import createAppGui
from sps.constant import *

if __name__ == '__main__':
    StartApp=createAppGui()
    StartApp.createMenuBar()
    StartApp.createHomeTab()
    app.mainloop()