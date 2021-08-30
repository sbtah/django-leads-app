from django.shortcuts import render, reverse
from .forms import AgentModelForm
from leads.models import Agent
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


class AgentListView(LoginRequiredMixin, ListView):

    template_name = 'agents/agent_list.html'
    queryset = Agent.objects.all()
    context_object_name = 'agents'


class AgentCreateView(LoginRequiredMixin, CreateView):

    template_name = 'agents/agent_create.html'
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse('agents:agent-list')

    def form_valid(self, form):
        agent = form.save(commit=False)
        agent.organisation = self.request.user.organisationprofile
        agent.save()
        return super(AgentCreateView, self).form_valid(form)
