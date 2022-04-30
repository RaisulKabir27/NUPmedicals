

# from django.test import TestCase, Client
# from django.urls import reverse
# from Hospital.models import Patient, Doctor, Emergency_Cabin
# from Hospital.views import index,show_doctors,doctor,show_profile,show_emergency,generate_prescription

# import json

# class TestViews(TestCase):


#     def test_show_doctors_GET(self):
        
#         client = Client()
#         response = client.get(reverse('show_doctors'))

#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'doctors.html')

#     def test_doctor_GET(self):
        
#         client = Client()
#         response = client.get(reverse('doctor'))

#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'doctor.html')

#     def test_show_emergency_GET(self):
        
#         client = Client()
#         response = client.get(reverse('show_emergency'))

#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'emergency.html')


#     def test_show_profile_GET(self):
        
#         client = Client()
#         response = client.get(reverse('show_profile'))

#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'profile.html')



    