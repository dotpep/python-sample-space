from web.forms import PanForm
from django.views.generic.edit import FormView
from web.models import Pan

class PanFormView(FormView):
    template_name = "pan_form.html"
    form_class = PanForm
    success_url = "/web/pans"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        Pan.objects.create(**form.cleaned_data)
        return super().form_valid(form)