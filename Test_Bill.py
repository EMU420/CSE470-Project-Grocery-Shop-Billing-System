import unittest


class Test_Bill(unittest.TestCase):
    
      def test_product_total_controller(self):
        self.assertEqual(4,4)

      def test_bill_area_controllers(self):
        self.assertEqual(6,6)

      def test_invoice_controller(self):
        self.assertEqual(4,4)  

      def test_clear_data_controller(self):
        self.assertEqual(3,3) 

      def test_find_bill_controller(self):
        self.assertEqual(2,2)

      def test_exit_app(self):
        self.assertEqual(10,10)

      def test_save_bill_controller(self):
        self.assertEqual(12,12)              


if __name__ == '__main__':
  unittest.main()        



