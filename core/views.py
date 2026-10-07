from django.shortcuts import render, redirect
from .models import Projeto, Tarefa
from .forms import ProjetoForm, TarefaForm

def lista_projetos(request):
    projetos = Projeto.objects.all()
    return render(request, 'projetos/lista.html', {'projetos': projetos})


def novo_projeto(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('lista_projetos')
    else:
        form = ProjetoForm()

    return render(request, 'projetos/form.html', {'form': form})

def editar_projeto(request, pk):
    projeto = Projeto.objects.get(id=pk)

    if request.method == 'POST':
        form = ProjetoForm(request.POST, instance=projeto)

        if form.is_valid():
            form.save()
            return redirect('lista_projetos')
    else:
        form = ProjetoForm(instance=projeto)

    return render(request, 'projetos/form.html', {'form': form})

def excluir_projeto(request, pk):
    projeto = Projeto.objects.get(id=pk)

    if request.method == 'POST':
        projeto.delete()
        return redirect('lista_projetos')

    return render(request, 'projetos/excluir.html', {'projeto': projeto})

def lista_tarefas(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'tarefas/lista.html', {'tarefas': tarefas})


def nova_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tarefas')
    else:
        form = TarefaForm()

    return render(request, 'tarefas/form.html', {'form': form})

def editar_tarefa(request, pk):
    tarefa = Tarefa.objects.get(id=pk)

    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('lista_tarefas')
    else:
        form = TarefaForm(instance=tarefa)

    return render(request, 'tarefas/form.html', {'form': form})

def excluir_tarefa(request, pk):
    tarefa = Tarefa.objects.get(id=pk)

    if request.method == 'POST':
        tarefa.delete()
        return redirect('lista_tarefas')

    return render(request, 'tarefas/excluir.html', {'tarefa': tarefa})