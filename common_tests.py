class CommonTests:
    def assertEqual(self, value1: any, value2: any):
        assert value1 == value2

    def assertIn(self, value1: any, value2: any):
        assert value1 in value2

    def assertDictEqual(self, value1: dict, value2: dict):
        assert value1 == value2

    def assertListEqual(self, value1: list, value2: list):
        assert value1 == value2

    def assertIsNotNone(self, value: any):
        assert value is not None

    def assertIsNone(self, value: any):
        assert value is None

    def assertTrue(self, value: bool):
        assert value is True

    def assertFalse(self, value: bool):
        assert value is False

    def assertDictContainsSubset(self, value1: dict, value2: dict):
        assert dict(value2, **value1) == value2
