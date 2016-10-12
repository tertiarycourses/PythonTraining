#!/usr/bin/python

class Point:
   def __init( self, x=0, y=0):
      self.x = x
      self.y = y
   def __del__(self):
      class_name = self.__class__.__name__
      print(class_name, "destroyed")

pt1 = Point()
pt2 = pt1
pt3 = pt1
del pt1
del pt2
del pt3