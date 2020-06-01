import unittest
import libraries.morflessLibs as libs

# import test values and expected outputs
# main includes sidebar data
import unit.read_schematic_test_io.read_schematic_1_test_io as tv1
import unit.read_schematic_test_io.read_schematic_2_test_io as tv2
import unit.read_schematic_test_io.read_schematic_3_test_io as tv3
import unit.read_schematic_test_io.read_schematic_4_test_io as tv4

from fixtures.decorators import testCall
# define settings element for test
settings = libs.globals.DEFAULT_SETTINGS

class ReadSchematicHandlerCase(unittest.TestCase):

    # set up and tear down reset to default settings
    def setUp(self):
        self.maxDiff= None
        self.settings = libs.string_processes.pcom_build_dictionary(libs.globals.DEFAULT_SETTINGS)

    def tearDown(self):
        self.settings = dict()

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

    @testCall
    def test_polimorf_determine_schematic_reference(self):

        for ind,test in enumerate(tv3.test_values_3):

            print('\n' + test['remark'] + '\n')

            inputs = test['inputs']

            out = libs.read_schematic.polimorf_determine_schematic_reference(
                        content=inputs['content'],
                        settings=inputs['settings'])

            print(out['processed'])
            print(out['schematic_content'])

            with self.subTest(i=ind+1):
                self.assertEqual(test['assertEqual']['processed'], out['processed'])
                self.assertEqual(test['assertEqual']['schematic_content'], out['schematic_content'])

    @testCall
    def test_get_settings(self):

        for ind,test in enumerate(tv3.test_values_4):

            print('\n' + test['remark'] + '\n')

            out = libs.read_schematic.get_settings(test['inputs']['content'])

            print(out)

            with self.subTest(i=ind+1):
                for test_key,test_val in test['assertEqual'].items():
                    self.assertEqual(test_val, out[test_key])

    @testCall
    def test_polimorf_process_schematic_sections(self):

        for ind,test in enumerate(tv4.test_values_5):

            print('\n' + test['remark'] + '\n')

            inputs = test['inputs']
            out = libs.read_schematic.polimorf_process_schematic_sections(
                        data=inputs['data'],
                        settings=inputs['settings'],
                        filename=inputs['filename'],
                        fileroot=inputs['fileroot'])

            print(out)

            with self.subTest(i=ind+1):
                self.assertEqual(test['assertEqual'].strip(), out.strip())

    @testCall
    def test_pcom_process_inserts(self):

        for ind,test in enumerate(tv4.test_values_6):

            print('\n' + test['remark'] + '\n')

            inputs = test['inputs']
            local_settings = inputs['settings']
            local_settings['add_settings_to_dependencies'] = inputs['add_settings_to_dependencies']

            (html_array,
            outlog,
            site_settings,
            dependencies) = libs.read_schematic.pcom_process_inserts(
                                    html_array=inputs['html_array'],
                                    insert_info=inputs['insert_info'],
                                    outlog=inputs['log'],
                                    site_settings=local_settings,
                                    filename=inputs['filename'],
                                    dependencies=inputs['dependencies'])

            print(html_array)

            with self.subTest(i=ind+1):
                self.assertEqual(test['assertEqual']['html_array'], html_array)
                self.assertEqual(test['assertEqual']['outlog'], outlog)
                self.assertEqual(test['assertEqual']['site_settings'], site_settings)
                self.assertEqual(test['assertEqual']['dependencies'], dependencies)
                self.assertEqual(test['assertEqual']['add_settings_to_dependencies'],
                    site_settings['add_settings_to_dependencies'])


if __name__ == '__main__':
    unittest.main()
