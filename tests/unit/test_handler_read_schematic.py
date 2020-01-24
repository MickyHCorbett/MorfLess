import unittest
import libraries.morflessLibs as libs

# import test values and expected outputs
# main includes sidebar data
from read_schematic_test_io.get_schematic_tags_test_io import test_values as gstags_tv

# define settings element for test
settings = libs.globals.DEFAULT_SETTINGS

class ReadSchematicHandlerCase(unittest.TestCase):

    def test_pcom_get_schematic_tags(self):

        for test in gstags_tv:

            print('\n' + test['remark'] + '\n')

            format = test['inputs']['format']
            print(format)

            result = libs.read_schematic.pcom_get_schematic_tags(format)
            print(result)

            # check asserts in
            for assertIn in test['assertIn']['meta']:
                self.assertIn(assertIn, result['meta'])
            for assertIn in test['assertIn']['header']:
                self.assertIn(assertIn, result['header'])
            for assertIn in test['assertIn']['before']:
                self.assertIn(assertIn, result['before'])
            for assertIn in test['assertIn']['main']:
                self.assertIn(assertIn, result['main'])
            for assertIn in test['assertIn']['after']:
                self.assertIn(assertIn, result['after'])
            for assertIn in test['assertIn']['sidebar']:
                self.assertIn(assertIn, result['sidebar'])
            for assertIn in test['assertIn']['footer']:
                self.assertIn(assertIn, result['footer'])

            # check asserts Not in
            for assertNotIn in test['assertNotIn']['meta']:
                self.assertNotIn(assertNotIn, result['meta'])
            for assertNotIn in test['assertNotIn']['header']:
                self.assertNotIn(assertNotIn, result['header'])
            for assertNotIn in test['assertNotIn']['before']:
                self.assertNotIn(assertNotIn, result['before'])
            for assertNotIn in test['assertNotIn']['main']:
                self.assertNotIn(assertNotIn, result['main'])
            for assertNotIn in test['assertNotIn']['after']:
                self.assertNotIn(assertNotIn, result['after'])
            for assertNotIn in test['assertNotIn']['sidebar']:
                self.assertNotIn(assertNotIn, result['sidebar'])
            for assertNotIn in test['assertNotIn']['footer']:
                self.assertNotIn(assertNotIn, result['footer'])

            # check equals
            self.assertEqual(test['assertEqual']['sidebar_found'], result['sidebar_found'])
            self.assertEqual(test['assertEqual']['before_found'], result['before_found'])
            self.assertEqual(test['assertEqual']['after_found'], result['after_found'])

        print('\n\n===== test_pcom_get_schematic_tags - END \n\n')

if __name__ == '__main__':
    unittest.main()
