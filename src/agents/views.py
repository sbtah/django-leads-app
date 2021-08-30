from django.shortcuts import render
from leads.models import Agent
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin


class AgentListView(LoginRequiredMixin, ListView):

    template_name = 'agents/agent_list.html'
    queryset = Agent.objects.all()
    context_object_name = 'agents'
