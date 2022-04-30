from django.test import SimpleTestCase
from Hospital.forms import CreateAppointment, UpdateInfo, UpdateDoctorForm, ApproveForm


class TestForms(SimpleTestCase):

    def test_CreateAppointment_no_data(self):
        form = CreateAppointment(data={})
        self.assertFalse(form.is_valid())

    def test_UpdateInfo_no_data(self):
        form = UpdateInfo(data={})
        self.assertFalse(form.is_valid())

    def test_UpdateDoctorForm_no_data(self):
        form = UpdateDoctorForm(data={})
        self.assertFalse(form.is_valid())

    def test_ApproveForm_no_data(self):
        form = ApproveForm(data={})
        self.assertFalse(form.is_valid())
















































    def test_Null1_no_data(self):
        form = CreateAppointment(data={})
        self.assertFalse(form.is_valid())

    def test_Null2_no_data(self):
        form = UpdateInfo(data={})
        self.assertFalse(form.is_valid())

    def test_Null3_no_data(self):
        form = UpdateDoctorForm(data={})
        self.assertFalse(form.is_valid())

    def test_Null4_no_data(self):
        form = ApproveForm(data={})
        self.assertFalse(form.is_valid())











