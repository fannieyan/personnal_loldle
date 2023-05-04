from django.test import SimpleTestCase
import game.utils as utils


class GameUtilsTestCase(SimpleTestCase):
    yuumi = {"champion": "Yuumi", "gender": "Female", "lanes": ["Support"], "species":
             ["Cat"], "resource": "Mana", "ranges": ["Range"], "regions": ["Bandle City", "Ionia"], "release_date": 2022}
    lulu = {"champion": "Lulu", "gender": "Female", "lanes": ["Support", "Top"], "species":
            ["Yordle"], "resource": "Mana", "ranges": ["Range", "Melee"], "regions": ["Bandle City"], "release_date": 2013}
    tahm_kench = {"champion": "Tahm Kench", "gender": "Male", "lanes": ["Top", "Bottom"], "species":
                  ["Something", "Cat"], "resource": "Tongue length", "ranges": ["Melee"], "regions": ["Ionia"], "release_date": 2023}

    def test_check_properties_yuumi_lulu(self):
        check_result = utils.check_properties(self.yuumi, self.lulu)
        expected = {
            "champion": utils.validity["NOT_VALID"],
            "gender": utils.validity["VALID"],
            "lanes": utils.validity["PARTIALLY_VALID"],
            "species": utils.validity["NOT_VALID"],
            "resource": utils.validity["VALID"],
            "ranges": utils.validity["PARTIALLY_VALID"],
            "regions": utils.validity["PARTIALLY_VALID"],
            "release_date": utils.comparison["MORE"],
        }
        print(check_result, expected)
        self.assertDictEqual(check_result, expected)

    def test_check_properties_yuumi_tahm(self):
        check_result = utils.check_properties(self.yuumi, self.tahm_kench)
        expected = {
            "champion": utils.validity["NOT_VALID"],
            "gender": utils.validity["NOT_VALID"],
            "lanes": utils.validity["NOT_VALID"],
            "species": utils.validity["PARTIALLY_VALID"],
            "resource": utils.validity["NOT_VALID"],
            "ranges": utils.validity["NOT_VALID"],
            "regions": utils.validity["PARTIALLY_VALID"],
            "release_date": utils.comparison["LESS"],
        }
        self.assertDictEqual(check_result, expected)

    def test_check_properties_yuumi_yuumi(self):
        check_result = utils.check_properties(self.yuumi, self.yuumi)
        expected = {
            "champion": utils.validity["VALID"],
            "gender": utils.validity["VALID"],
            "lanes": utils.validity["VALID"],
            "species": utils.validity["VALID"],
            "resource": utils.validity["VALID"],
            "ranges": utils.validity["VALID"],
            "regions": utils.validity["VALID"],
            "release_date": utils.comparison["EQUAL"],
        }
        self.assertDictEqual(check_result, expected)
