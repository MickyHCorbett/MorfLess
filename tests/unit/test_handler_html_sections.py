import unittest

import libraries.morflessLibs as libs

# import test values and expected outputs
# main includes sidebar data
from unit.html_sections_test_io.main_test_io import test_values as main_tv
from unit.html_sections_test_io.header_test_io import test_values as header_tv
from unit.html_sections_test_io.footer_test_io import test_values as footer_tv
from unit.html_sections_test_io.before_test_io import test_values as before_tv
from unit.html_sections_test_io.after_test_io import test_values as after_tv

from fixtures.decorators import testCall

# define settings element for test
settings = libs.globals.DEFAULT_SETTINGS

class HtmlSectionsHandlerCase(unittest.TestCase):

    @testCall
    def test_polimorf_add_main(self):

        for ind,test in enumerate(main_tv):

            print('\n' + test['remark'] + '\n')

            main_data = test['inputs']['main_data']
            sidebar_data = test['inputs']['sidebar_data']
            meta_present = test['inputs']['meta_present']
            wrap = test['inputs']['wrap']
            fileroot = test['inputs']['fileroot']
            is_template = test['inputs']['is_template']
            is_search = test['inputs']['is_search']

            result = libs.main.polimorf_add_main(main_data,sidebar_data,meta_present,wrap,fileroot,settings,is_template,is_search)
            print(result)

            # check asserts in
            with self.subTest(i=ind+1):
                for assertIn in test['assertIn']:
                    self.assertIn(assertIn, result)

                # check asserts Not in
                for assertNotIn in test['assertNotIn']:
                    self.assertNotIn(assertNotIn, result)


    @testCall
    def test_polimorf_add_header(self):

        for ind,test in enumerate(header_tv):

            print('\n' + test['remark'] + '\n')

            header_data = test['inputs']['header_data']
            meta_present = test['inputs']['meta_present']

            result = libs.header.polimorf_add_header(header_data,meta_present)
            print(result)

            # check asserts in
            with self.subTest(i=ind+1):
                for assertIn in test['assertIn']:
                    self.assertIn(assertIn, result)

                # check asserts Not in
                for assertNotIn in test['assertNotIn']:
                    self.assertNotIn(assertNotIn, result)


    @testCall
    def test_polimorf_add_footer(self):

        for ind,test in enumerate(footer_tv):

            print('\n' + test['remark'] + '\n')

            footer_data = test['inputs']['footer_data']
            meta_present = test['inputs']['meta_present']

            result = libs.footer.polimorf_add_footer(footer_data,meta_present)
            print(result)

            # check asserts in
            with self.subTest(i=ind+1):
                for assertIn in test['assertIn']:
                    self.assertIn(assertIn, result)

                # check asserts Not in
                for assertNotIn in test['assertNotIn']:
                    self.assertNotIn(assertNotIn, result)


    @testCall
    def test_polimorf_add_before(self):

        for ind,test in enumerate(before_tv):

            print('\n' + test['remark'] + '\n')

            before_data = test['inputs']['before_data']
            sidebar_data = test['inputs']['sidebar_data']
            meta_present = test['inputs']['meta_present']


            result = libs.before_after.polimorf_add_before(before_data,sidebar_data,meta_present)
            print(result)

            with self.subTest(i=ind+1):
                # check asserts in
                for assertIn in test['assertIn']:
                    self.assertIn(assertIn, result)

                # check asserts Not in
                for assertNotIn in test['assertNotIn']:
                    self.assertNotIn(assertNotIn, result)


    @testCall
    def test_polimorf_add_after(self):

        for ind,test in enumerate(after_tv):

            print('\n' + test['remark'] + '\n')

            after_data = test['inputs']['after_data']
            meta_present = test['inputs']['meta_present']
            sidebar_data = test['inputs']['sidebar_data']
            wrap = test['inputs']['wrap']

            result = libs.before_after.polimorf_add_after(after_data,sidebar_data,meta_present,wrap)
            print(result)

            with self.subTest(i=ind+1):
                # check asserts in
                for assertIn in test['assertIn']:
                    self.assertIn(assertIn, result)

                # check asserts Not in
                for assertNotIn in test['assertNotIn']:
                    self.assertNotIn(assertNotIn, result)
                    

if __name__ == '__main__':
    unittest.main()
