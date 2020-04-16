from tkinter import *
import time
import window
class UIManager():
    def __init__(self, frame: window.Window):
        self.frame = frame
        self.is_in_darkmode = False
        self.current_resolution = [800,600]
        self.maximum_resolution = (3840,2160)
    @property
    def is_fullscreen(self):
        return tuple(self.current_resolution) == self.maximum_resolution
    def resize_window(self, target_resolution):
      tar_x, tar_y = target_resolution
      max_x, max_y = self.maximum_resolution
      if tar_x > max_x or tar_y > max_y:
        return
      self.frame.resize_to()
