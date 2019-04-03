from django.views.generic import TemplateView

from .forms import CalcForm


class CalcView(TemplateView):
    template_name = "app/calc.html"

    def get(self, request, *args, **kwargs):
        form = CalcForm(request.GET)

        summa = int(request.GET.get('initial_fee', 0))
        percent = int(request.GET.get('rate', 0)) / 100
        months = int(request.GET.get('months_count', 1))

        common_result = summa + summa * percent
        result = common_result / months

        context = {
            'form': form,
            'result': result,
            'common_result': common_result
        }

        return self.render_to_response(context)
