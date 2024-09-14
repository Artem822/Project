from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView


class test(TemplateView):
    template_name = 'base.html'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        return super().get_context_data(**kwargs)
