from django import forms
from .models import *
from account.forms import FormSettings


class VoterForm(FormSettings):
    class Meta:
        model = Voter
        fields = ["email"]


class PositionForm(FormSettings):
    class Meta:
        model = Position
        fields = ["name"]


class CandidateForm(FormSettings):
    class Meta:
        model = Candidate
        fields = ["fullname", "position", "photo"]
