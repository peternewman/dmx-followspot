#!/usr/bin/env python
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Library General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# dmx_followspot.py
# Copyright (C) 2018 Branson Matheson    

import os
import yaml
import pprint

SCENE_FILE='scenes.yml'
# matches 
SCENE_COUNT=255

class Scene:
    def __init__(self, scene):
        self.scene = scene
        self.x = scene['x']

class Scenes:
    ''' 
    Scenes .. and object that has all the scenes for an instance
    '''
    def __init__(self, path=SCENE_FILE):
        self.path = path
        self.read()

    def read(self):
        if os.path.exists(self.path):
            log.info('reading %s' % path)
            with open(path, 'r') as stream:
                self.scenes = yaml.load(stream)
        else:
            # initialize array
            self.scenes = []
            for i in range(SCENE_COUNT):
                self.scenes.append(dict(
                    name='',
                    fixture_group='',
                    x=0,
                    y=0,
                    ))
        return self.scenes  


    def write(self):
         with open(path, 'w') as yaml_file:
             yaml.dump(self.scenes, yaml_file, default_flow_style=False)
             
    
    def get(self,id):
        return Scene(self.scenes[id])
