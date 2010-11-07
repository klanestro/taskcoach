'''
Task Coach - Your friendly task manager
Copyright (C) 2004-2010 Task Coach developers <developers@taskcoach.org>

Task Coach is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Task Coach is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import test
from taskcoachlib import gui, command, config, persistence
from taskcoachlib.domain import note, attachment


class TemplatesDialogUnderTest(gui.dialog.templates.TemplatesDialog):
    def _loadTemplates(self):
        return []
    

class TemplatesDialogTestCase(test.wxTestCase):
    def setUp(self):
        super(TemplatesDialogTestCase, self).setUp()
        self.settings = config.Settings(load=False)
        self.taskFile = persistence.TaskFile()
        self.editor = TemplatesDialogUnderTest(self.settings, self.frame, 
            'title', raiseDialog=False)

    def testTwoDefaultTemplates(self):
        self.assertEqual(0, len(self.editor.tasks))
