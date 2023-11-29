import unittest
import requests
import json

class Numbers(unittest.TestCase):

    def test_api_1(self):
        cevap = requests.get("https://automationexercise.com/api/productsList")
        print(cevap.text)

    def test_api_2(self):
        payload = {"key1": "value1"}
        cevap = requests.post("https://automationexercise.com/api/productsList", data=payload)
        print(cevap.text)
        print(cevap.status_code)


    def test_api_3(self):
        cevap = requests.get("https://automationexercise.com/api/brandsList")

        # Yanıtı kontrol etme
        if cevap.status_code == 200:
            print(cevap.status_code)
            print(cevap.json())

    def test_api_4(self):

        cevap = requests.put("https://automationexercise.com/api/brandsList")
        print(cevap.text)

    def test_api_5(self):
        payload = {"search_product": "top"}
        gonder = requests.post("https://automationexercise.com/api/searchProduct", data=payload)
        icerik = json.loads(gonder.text)
        self.assertEqual("Tops", icerik["products"][0]["category"]["category"])
        print(gonder.status_code)

    def ttest_api_6(self):
        payload = {"email": "example@gmail.com", "password": "12345"}
        response = requests.post("https://automationexercise.com/api/verifyLogin", data=payload)
        self.assertEqual(200, response.status_code)
        content = json.loads(response.text)
        self.assertIn("message", content)


    def test_api_7_8(self):
        api_url = "https://automationexercise.com/api/verifyLogin"
        request_data = {
            "email": "example@example.com",
            "password": "123"
        }

        cevap = requests.post(api_url, data=request_data)

        self.assertEqual(cevap.status_code, 200, "User exists!")
        self.assertEqual(cevap.json()["message"], "User not found!")

    def test_api_9(self):
        api_url = "https://automationexercise.com/api/verifyLogin"
        request_data = {
            "email": "example@example.com",
            "password": "123"
        }

        cevap = requests.delete(api_url, data=request_data)
        self.assertEqual(cevap.status_code, 405, "not supported!")

    def test_api_10(self):

        request_data = {
            "email": "invalid@example.com",
            "password": "invalidpassword"
        }

        response = requests.post("https://automationexercise.com/api/verifyLogin", data=request_data)
        self.assertEqual(404, response.status_code, "user not found")


    def test_api_11(self):

        request_data = {
            "name": "John Doe",
            "email": "john.doe@example.com",
            "password": "securepassword",
            "title": "Mr",
            "birth_date": "01",
            "birth_month": "01",
            "birth_year": "1990",
            "firstname": "John",
            "lastname": "Doe",
            "company": "ABC Corp",
            "address1": "123 Main Street",
            "address2": "Apt 45",
            "country": "United States",
            "zipcode": "12345",
            "state": "CA",
            "city": "Los Angeles",
            "mobile_number": "1234567890"
        }

        response = requests.post("https://automationexercise.com/api/createAccount", data=request_data)

        self.assertEqual(201, response.status_code, "User created!")

    def test_api_12(self):
        request_data = {
            "email": "invalid@example.com",
            "password": "invalidpassword"
        }

        cevap= requests.delete("https://automationexercise.com/api/updateAccount", data=request_data)
        self.assertEqual(200, cevap.status_code, "User update!")


    def test_api_13(self):

        request_data = {
            "name": "John Doe",
            "email": "john.doe@example.com",
            "password": "newpassword",
            "title": "Mr",
            "birth_date": "01",
            "birth_month": "01",
            "birth_year": "1990",
            "firstname": "John",
            "lastname": "Doe",
            "company": "New Corp",
            "address1": "456 Main Street",
            "address2": "Apt 67",
            "country": "United States",
            "zipcode": "54321",
            "state": "NY",
            "city": "New York",
            "mobile_number": "9876543210"
        }

        response = requests.put("https://automationexercise.com/api/updateAccount", data=request_data)
        self.assertEqual(200, response.status_code)
        content = response.json()
        self.assertIn("message", content)

        if "message" in content:
            expected_message = "User updated!"
            self.assertEqual(expected_message, content["message"])

    def test_api_14(self):
        request_params = {
            "email": "user@example.com"
        }

        response = requests.get("https://automationexercise.com/api/getUserDetailByEmail", params=request_params)
        self.assertEqual(200, response.status_code)
        content = response.json()

        self.assertIn("user_id", content)
        self.assertIn("name", content)



if __name__ == '__main__':
    unittest.main()

"""python3 -m unittest exampleTest.Numbers.test_api_get3"""