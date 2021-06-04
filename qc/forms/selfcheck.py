from django import forms
from qc.models import Project, Category, WorkList, Question, Choice, Task


class ProjectAddForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['sn', 'name', 'sponsor', 'loc_county', 'loc_area', 'starttime', 'endtime', 'editor', 'remark']
        widgets = {
            'sn': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'sponsor': forms.Select(attrs={'class': 'custom-select'}),
            'loc_county': forms.TextInput(attrs={'class': 'form-control'}),
            'loc_area': forms.TextInput(attrs={'class': 'form-control'}),
            'starttime': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'endtime': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'remark': forms.Textarea(attrs={'class': 'form-control'}),
        }


class ProjectUpdateForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['name', 'sponsor', 'loc_county', 'loc_area', 'starttime', 'endtime', 'remark']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'sponsor': forms.Select(attrs={'class': 'custom-select'}),
            'loc_county': forms.TextInput(attrs={'class': 'form-control'}),
            'loc_area': forms.TextInput(attrs={'class': 'form-control'}),
            'starttime': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'endtime': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'remark': forms.Textarea(attrs={'class': 'form-control'}),
        }


class CateAddForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['proj', 'name', 'sponsor', 'starttime', 'endtime', 'remark', 'editor']
        widgets = {
            'name': forms.Select(attrs={'class': 'custom-select'}),
            'sponsor': forms.Select(attrs={'class': 'custom-select'}),
            'starttime': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'endtime': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'remark': forms.Textarea(attrs={'class': 'form-control'}),
        }


class CateUpdateForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['sponsor', 'starttime', 'endtime', 'remark', 'editor']
        widgets = {
            'sponsor': forms.Select(attrs={'class': 'custom-select'}),
            'starttime': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'endtime': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'remark': forms.Textarea(attrs={'class': 'form-control'}),
        }


class WorkListAddForm(forms.ModelForm):

    class Meta:
        model = WorkList
        fields = ['cate', 'subcate', 'timing', 'name', 'contractor', 'sponsor', 'starttime',
                  'endtime', 'remark', 'editor']
        widgets = {
            'subcate': forms.Select(attrs={'class': 'custom-select'}),
            'timing': forms.Select(attrs={'class': 'custom-select'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'contractor': forms.Select(attrs={'class': 'custom-select'}),
            'sponsor': forms.Select(attrs={'class': 'custom-select'}),
            'starttime': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'endtime': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'remark': forms.Textarea(attrs={'class': 'form-control'}),
        }


class WorkListUpdateForm(forms.ModelForm):

    class Meta:
        model = WorkList
        fields = ['sponsor', 'name', 'contractor', 'starttime', 'endtime', 'remark', 'editor']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'sponsor': forms.Select(attrs={'class': 'custom-select'}),
            'contractor': forms.Select(attrs={'class': 'custom-select'}),
            'starttime': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'endtime': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'remark': forms.Textarea(attrs={'class': 'form-control'}),
        }


class QuestionAddForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ['worklist', 'category', 'title', 'abstract', 'type', 'rank', 'ordering', 'is_required', 'editor',
                  'goodimg', 'badimg', 'method', 'improvement']
        widgets = {
            'category': forms.Select(attrs={'class': 'custom-select'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'abstract': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'custom-select'}),
            'rank': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5}),
            'method': forms.TextInput(attrs={'class': 'form-control'}),
            'goodimg': forms.ClearableFileInput(attrs={'class': 'custom-file-input'}),
            'badimg': forms.ClearableFileInput(attrs={'class': 'custom-file-input'}),
            'ordering': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'is_required': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'improvement': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ChoiceAddForm(forms.ModelForm):

    class Meta:
        model = Choice
        fields = '__all__'
        widgets = {
            'desc': forms.TextInput(attrs={'class': 'form-control'}),
        }


class TaskAddForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['worklist', 'sponsor', 'count', 'sched_time', 'editor']
        widgets = {
            'sponsor': forms.Select(attrs={'class': 'custom-select'}),
            'count': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'sched_time': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }


