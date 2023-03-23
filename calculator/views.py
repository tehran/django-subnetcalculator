from django.shortcuts import render
from .forms import SubnetCalculatorForm
from ipaddress import IPv4Interface

def subnet_calculator(request):
    if request.method == 'POST':
        form = SubnetCalculatorForm(request.POST)

        if form.is_valid():
            ip_address = form.cleaned_data['ip_address']
            subnet_mask = form.cleaned_data['subnet_mask']

            subnet = IPv4Interface(f"{ip_address}/{subnet_mask}")
            network = subnet.network
            num_hosts = network.num_addresses - 2
            wildcard_mask = subnet.hostmask
            first_available_host = network.network_address + 1
            last_available_host = network.broadcast_address - 1

            context = {
                'subnet': network,
                'num_hosts': num_hosts,
                'wildcard_mask': wildcard_mask,
                'first_available_host': first_available_host,
                'last_available_host': last_available_host,
                'form': form,
            }
            return render(request, 'calculator/subnet_calculator.html', context)
    else:
        form = SubnetCalculatorForm()

    return render(request, 'calculator/subnet_calculator.html', {'form': form})
