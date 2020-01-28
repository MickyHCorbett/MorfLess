import unittest

# import test values and expected outputs
# main includes sidebar data
from unit.test_handler_html_sections import HtmlSectionsHandlerCase
from unit.test_handler_read_schematic import ReadSchematicHandlerCase
from unit.test_handler_string_processes_1 import StringProcesses1HandlerCase
from unit.test_handler_string_processes_2 import StringProcesses2HandlerCase
from unit.test_handler_lists_1 import ListsHandler1Case

def suite():
    suite = unittest.TestSuite()
    suite.addTest(HtmlSectionsHandlerCase())
    suite.addTest(ReadSchematicHandlerCase())
    suite.addTest(StringProcesses1HandlerCase())
    suite.addTest(StringProcesses2HandlerCase())
    suite.addTest(ListsHandler1Case())
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
