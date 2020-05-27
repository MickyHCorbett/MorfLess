import unittest
import libraries.morflessLibs as libs

# import test values and expected outputs
# main includes sidebar data
import unit.read_schematic_test_io.read_schematic_1_test_io as tv1
import unit.read_schematic_test_io.read_schematic_2_test_io as tv2
import unit.read_schematic_test_io.read_schematic_3_test_io as tv3

from fixtures.decorators import testCall
# define settings element for test
settings = libs.globals.DEFAULT_SETTINGS

class ReadSchematicHandlerCase(unittest.TestCase):

    @testCall
    def test_pcom_get_schematic_tags(self):

        for ind,test in enumerate(tv1.test_values):

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

    @testCall
    def test_pcom_determine_placement(self):

        for ind,test in enumerate(tv2.test_values):

            print('\n' + test['remark'] + '\n')

            placement = test['inputs']['placement']
            print(format)

            result = libs.read_schematic.pcom_determine_placement(placement)
            print(result)

            # check asserts in
            for assertIn in test['assertIn']:
                self.assertIn(assertIn, result)

            # check asserts Not in
            for assertNotIn in test['assertNotIn']:
                self.assertNotIn(assertNotIn, result)

    @testCall
    def test_polimorf_process_settings_schematic(self):

        for ind,test in enumerate(tv3.test_values_1):

            print('\n' + test['remark'] + '\n')

            inputs = test['inputs']

            out,test_settings = libs.read_schematic.polimorf_process_settings_schematic(
                        schematic=inputs['schematic'],
                        args=inputs['args'],
                        placement=inputs['placement'],
                        type=inputs['type'],
                        settings=inputs['settings'])

            print(out)
            print(f"{test['test_val']} - {test_settings[test['test_val']]}")

            with self.subTest(i=ind+1):
                self.assertEqual(test['assertEqual']['out'], out)
                self.assertEqual(test['assertEqual'][test['test_val']], test_settings[test['test_val']])

    @testCall
    def test_polimorf_process_additions_schematic(self):

        for ind,test in enumerate(tv3.test_values_2):

            print('\n' + test['remark'] + '\n')

            inputs = test['inputs']

            out = libs.read_schematic.polimorf_process_additions_schematic(
                        schematic=inputs['schematic'],
                        args=inputs['args'],
                        placement=inputs['placement'],
                        type=inputs['type'])

            print(out)

            with self.subTest(i=ind+1):
                self.assertEqual(test['assertEqual']['out'], out)

if __name__ == '__main__':
    unittest.main()
