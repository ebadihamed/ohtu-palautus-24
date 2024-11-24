import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.varasto_mock = Mock()
        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        # palautetaan aina arvo 42
        self.viitegeneraattori_mock.uusi.return_value = 1

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 10
            if tuote_id == 3:
                return 0

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(1, "leipä", 10)
            if tuote_id == 3:
                return Tuote(1, "auto", 200)

        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
    
    def test_tilisiirto_kutsutaan_oikeat_arvot(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistus
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 1, "12345", "33333-44455", 5)
    
    def test_kaksi_eri_tuotetta(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "1111")

        # varmistus
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 1, "1111",  "33333-44455", 15)    
    
    def test_kaksi_samaa_tuotetta(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "1111")

        # varmistus
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 1, "1111",  "33333-44455", 20)

    def test_tuotetta_ei_ole_varastossa(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("pekka", "1111")

        # varmistus
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 1, "1111",  "33333-44455", 10)   

    def test_poista_tuote_toimii(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.poista_korista(1)
        self.kauppa.tilimaksu("pekka", "1111")

        # varmistus
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 1, "1111",  "33333-44455", 0) 


    def test_alustus_toimii(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "1111")

        # varmistus
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 1, "1111",  "33333-44455", 15)   

    def test_viitegenerattori_toimii(self):
        viitegeneraattori_mock = Mock(wraps=Viitegeneraattori())
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("pekka", "11")
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("hamed", "2222")

        self.pankki_mock.tilisiirto.assert_called_with("hamed", 3, "2222",  ANY, ANY)   
    

