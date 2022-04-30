from django.test import SimpleTestCase
from django.urls import reverse, resolve
from Hospital.views import show_doctors, index, doctor, generate_prescription, show_profile, show_emergency

class TestUrls(SimpleTestCase):

    def test_show_doctor_is_resolved(self):
        url = reverse('doctors')
       
        self.assertEquals(resolve(url).func, show_doctors)

    def test_index_is_resolved(self):
        url = reverse('index')
       
        self.assertEquals(resolve(url).func, index)

    # def test_doctor_is_resolved(self):
    #     url = reverse('doctor')
        
    #     self.assertEquals(resolve(url).func, doctor)

    def test_generate_prescription_is_resolved(self):
        url = reverse('generate_prescription')
       
        self.assertEquals(resolve(url).func, generate_prescription)

    def test_show_profile_is_resolved(self):
        url = reverse('profile')
        
        self.assertEquals(resolve(url).func, show_profile)


    def test_show_emergency_is_resolved(self):
        url = reverse('emergency')
       
        self.assertEquals(resolve(url).func, show_emergency)  












    def test_index1_is_resolved(self):
        url = reverse('index')
       
        self.assertEquals(resolve(url).func, index)

    def test_index2_is_resolved(self):
        url = reverse('index')
       
        self.assertEquals(resolve(url).func, index)







    def test_show_profile1_is_resolved(self):
        url = reverse('profile')
        
        self.assertEquals(resolve(url).func, show_profile)


    def test_show_emergency1_is_resolved(self):
        url = reverse('emergency')
       
        self.assertEquals(resolve(url).func, show_emergency)        
