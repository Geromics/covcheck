import sys
import unittest
sys.path.insert(0, '/Users/tanvisingh/Documents/Geromics/covcheck')
from Osteoarthritis import Osteo

class TestSNP_age(unittest.TestCase):
    def test_snp(self):
        Ot = Osteo()
        data = Ot.read_json_individual()
        assert data['age'] == 44
        assert list(data['snps'].keys())[0]== 'rs6976'
        assert list(data['snps'].keys())[0] == 'rs835488'
        assert data['id'] =='dan.geromics'
        data1= Ot.read_json_osteo()
        assert data1['trait']=='Osteoarthritis'
        #assert list(data1['groups'])[1]== '44'
if __name__ == '__main__':
    unittest.main()
    test_snp()