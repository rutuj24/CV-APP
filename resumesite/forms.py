from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Submit
from crispy_forms.layout import Column
from crispy_forms.layout import Row

class ContactForm(forms.Form):
	name=forms.CharField()#required=False
	email=forms.EmailField(label='E-Mail')
	mobile=forms.CharField()
	address=forms.CharField(required=False)
	desc=forms.CharField(label='Description')
	skills_1=forms.CharField()
	skills_2=forms.CharField()
	skills_3=forms.CharField()
	skills_4=forms.CharField()
	skills_5=forms.CharField(required=False)
	skills_6=forms.CharField(required=False)

	experience_1_title=forms.CharField()
	experience_1_dur=forms.CharField()
	experience_1_desc=forms.CharField()

	experience_2_title=forms.CharField(required=False)
	experience_2_dur=forms.CharField(required=False)
	experience_2_desc=forms.CharField(required=False)

	education_10th_year=forms.CharField()
	education_10th_uni=forms.CharField()
	education_10th_score=forms.CharField()

	education_12th_year=forms.CharField()
	education_12th_uni=forms.CharField()
	education_12th_score=forms.CharField()

	education_btech_year=forms.CharField()
	education_btech_uni=forms.CharField()
	education_btech_score=forms.CharField()

	education_mtech_year=forms.CharField(required=False)
	education_mtech_uni=forms.CharField(required=False)
	education_mtech_score=forms.CharField(required=False)


	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.helper=FormHelper
		self.helper.form_class = ' container justify-content-center '
		self.helper.form_method="post"
		self.helper.layout=Layout(
			Row(
                Column('name', css_class='form-group col-md-5  mb-10'),
                Column('email', css_class='form-group col-md-7 mb-10'),
                css_class='form-row  center'
            ),
			Row(
                Column('mobile', css_class='form-group col-md-5  mb-10'),
                Column('address', css_class='form-group col-md-7 mb-10'),
                css_class='form-row  center'
            ),
			Row(
                Column('desc', css_class='form-group col-md-12  mb-10'),
                css_class='form-row  center'
            ),
			Row(
                Column('skills_1', css_class='form-group col-md-6  mb-10'),
                Column('skills_2', css_class='form-group col-md-6 mb-10'),
                css_class='form-row  center'
            ),
			Row(
                Column('skills_3', css_class='form-group col-md-6  mb-10'),
                Column('skills_4', css_class='form-group col-md-6 mb-10'),
                css_class='form-row  center'
            ),
			Row(
                Column('skills_5', css_class='form-group col-md-6  mb-10'),
                Column('skills_6', css_class='form-group col-md-6 mb-10'),
                css_class='form-row  center'
            ),
			Row(
                Column('experience_1_title', css_class='form-group col-md-7  mb-10'),
                Column('experience_1_dur', css_class='form-group col-md-5 mb-10'),
                css_class='form-row  center'
            ),
			'experience_1_desc',
			Row(
                Column('experience_2_title', css_class='form-group col-md-7  mb-10'),
                Column('experience_2_dur', css_class='form-group col-md-5 mb-10'),
                css_class='form-row  center'
            ),
			'experience_2_desc',
			Row(
                Column('education_10th_year', css_class='form-group col-md-3 mb-10'),
                Column('education_10th_score', css_class='form-group col-md-3 mb-10'),
		        Column('education_10th_uni', css_class='form-group col-md-6 mb-10'),
                css_class='form-row  center'
            ),
			Row(
                Column('education_12th_year', css_class='form-group col-md-3 mb-10'),
                Column('education_12th_score', css_class='form-group col-md-3 mb-10'),
		        Column('education_12th_uni', css_class='form-group col-md-6 mb-10'),
                css_class='form-row  center'
            ),
			Row(
                Column('education_btech_year', css_class='form-group col-md-3 mb-10'),
                Column('education_btech_score', css_class='form-group col-md-3 mb-10'),
		        Column('education_btech_uni', css_class='form-group col-md-6 mb-10'),
                css_class='form-row  center'
            ),
			Row(
                Column('education_mtech_year', css_class='form-group col-md-3 mb-10'),
                Column('education_mtech_score', css_class='form-group col-md-3 mb-10'),
		        Column('education_mtech_uni', css_class='form-group col-md-6 mb-10'),
                css_class='form-row  center'
            ),
			Submit('submit','Submit',css_class="btn-success")
			)