import unittest

# import test values and expected outputs
# main includes sidebar data
from unit.test_handler_html_sections import HtmlSectionsHandlerCase
from unit.test_handler_read_schematic import ReadSchematicHandlerCase
from unit.test_handler_string_processes_1 import StringProcesses1HandlerCase
from unit.test_handler_string_processes_2 import StringProcesses2HandlerCase
from unit.test_handler_lists_1 import ListsHandler1Case
from unit.test_handler_meta_elements import MetaElementsCase

from mockAws.test_handler_bucket_operations import RenderHtmlBucketOperations
from mockAws.test_handler_bucket_operations import CreateListPagesBucketOperations
from mockAws.test_handler_bucket_operations import SearchContentBucketOperations

def suite():
    suite = unittest.TestSuite()
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
