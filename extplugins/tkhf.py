#
# BigBrotherBot(B3) (www.bigbrotherbot.net)
# Copyright (C) 2011 
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#
# CHANGELOG
# 
# 2011-05-01 - 1.0 - Courgette
# * first release
# 2011-06-04 - 1.1 - Courgette
# * update plugin due to changes in Homefront 1.0.4 patch
#
__version__ = '1.1'
__author__  = 'Courgette'

from b3.plugin import Plugin
from b3.events import EVT_CLIENT_KILL_TEAM

class TkhfPlugin(Plugin):
    requiresConfigFile = False
    
    def onStartup(self):
        self.registerEvent(EVT_CLIENT_KILL_TEAM)

    def onEvent(self, event):
        if event.type == EVT_CLIENT_KILL_TEAM:
            self.console.write('admin kill "%s"' % event.client.guid)


if __name__ == '__main__':
    import time
    from b3.fake import fakeConsole, joe, simon
    from b3 import TEAM_BLUE
    
    p = TkhfPlugin(fakeConsole)
    p.onStartup() 
    
    joe.team = TEAM_BLUE
    simon.team = TEAM_BLUE
    
    print('-'*30)
    joe.kills(simon)
    time.sleep(6)
    