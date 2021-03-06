from django import forms
from django.forms import ModelForm
from ticket.models import Project, Ticket, Workflow, Reply
from django.utils.text import slugify


class TicketForm(ModelForm):

    class Meta:
        model = Ticket
        fields = ['name', 'description', 'type', 'high_priority', 'project']
        widgets = {
            'name': forms.TextInput(attrs={'id': 'project-name', 'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control new-ticket', 'rows': 4}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'project': forms.Select(attrs={'class': 'form-control'})
        }

    def save(self):
        instance = super(TicketForm, self).save(commit=False)
        instance.slug = slugify(instance.name)
        instance.save()

        return instance


class AssignToForm(forms.ModelForm):
    class Meta:
        model = Workflow
        fields = ['comment', 'current_status', 'post_status', 'ticket', 'user']
        widgets = {
            'comment': forms.Textarea(attrs={'class': 'form-control span8', 'rows': 4}),
            'current_status': forms.HiddenInput(),
            'post_status': forms.HiddenInput(),
            'ticket': forms.HiddenInput(),
            'user': forms.Select(attrs={'class': 'form-control'})
        }


class CancelForm(forms.ModelForm):
    class Meta:
        model = Workflow
        fields = ['comment', 'current_status', 'post_status', 'ticket', 'user']
        widgets = {
            'comment': forms.Textarea(attrs={'class': 'form-control span8', 'rows': 4}),
            'current_status': forms.HiddenInput(),
            'post_status': forms.HiddenInput(),
            'ticket': forms.HiddenInput(),
            'user': forms.HiddenInput()
        }


class ReopenForm(forms.ModelForm):
    class Meta:
        model = Workflow
        fields = ['comment', 'current_status', 'post_status', 'ticket', 'user']
        widgets = {
            'comment': forms.Textarea(attrs={'class': 'form-control span8', 'rows': 4}),
            'current_status': forms.HiddenInput(),
            'post_status': forms.HiddenInput(),
            'ticket': forms.HiddenInput(),
            'user': forms.HiddenInput()
        }


class SolveForm(forms.ModelForm):
    class Meta:
        model = Workflow
        fields = ['comment', 'current_status', 'post_status', 'ticket', 'user']
        widgets = {
            'comment': forms.Textarea(attrs={'class': 'form-control span8', 'rows': 4}),
            'current_status': forms.HiddenInput(),
            'post_status': forms.HiddenInput(),
            'ticket': forms.HiddenInput(),
            'user': forms.HiddenInput()
        }


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['comment', 'ticket', 'user']
        widgets = {
            'comment': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Comment ...'}),
            'ticket': forms.HiddenInput(),
            'user': forms.HiddenInput()
        }
