# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PortfolioForm, ProjectForm, SkillForm
from .models import Portfolio, Project, Skill

@login_required(login_url='/login')
def create_portfolio(request):
    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES)
        if form.is_valid():
            portfolio = form.save(commit=False)
            portfolio.user = request.user
            portfolio.save()
            return redirect('portfolio-list')
    else:
        form = PortfolioForm()
    return render(request, 'portfolio/portfolio_form.html', {'form': form})



# views.py
@login_required(login_url='/login')
def update_portfolio(request, pk):
    portfolio = Portfolio.objects.get(pk=pk, user=request.user)
    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES, instance=portfolio)
        if form.is_valid():
            form.save()
            return redirect('portfolio-list')
    else:
        form = PortfolioForm(instance=portfolio)
    return render(request, 'portfolio/portfolio_form.html', {'form': form})



# views.py
@login_required(login_url='/login')
def delete_portfolio(request, pk):
    portfolio = Portfolio.objects.get(pk=pk, user=request.user)
    if request.method == 'POST':
        portfolio.delete()
        return redirect('portfolio-list')
    return redirect('profile')


# views.py
@login_required(login_url='/login')
def portfolio_list(request):
    portfolios = Portfolio.objects.filter(user=request.user)
    return render(request, 'portfolio/portfolio_list.html', {'portfolios': portfolios})





@login_required
def create_project(request, portfolio_id):
    portfolio = Portfolio.objects.get(id=portfolio_id, user=request.user)
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.portfolio = portfolio
            project.save()
            return redirect('portfolio-detail', pk=portfolio_id)
    else:
        form = ProjectForm()
    return render(request, 'portfolio/project_form.html', {'form': form})




@login_required
def update_project(request, pk):
    project = Project.objects.get(pk=pk, portfolio__user=request.user)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('portfolio-detail', pk=project.portfolio.id)
    else:
        form = ProjectForm(instance=project)
    return render(request, 'portfolio/project_form.html', {'form': form})



@login_required
def delete_project(request, pk):
    project = Project.objects.get(pk=pk, portfolio__user=request.user)
    if request.method == 'POST':
        project.delete()
        return redirect('portfolio-detail', pk=project.portfolio.id)
    return render(request, 'portfolio/project_confirm_delete.html', {'project': project})



@login_required
def create_skill(request, portfolio_id):
    portfolio = Portfolio.objects.get(id=portfolio_id, user=request.user)
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.portfolio = portfolio
            skill.save()
            return redirect('portfolio-detail', pk=portfolio_id)
    else:
        form = SkillForm()
    return render(request, 'portfolio/skill_form.html', {'form': form})



@login_required
def update_skill(request, pk):
    skill = Skill.objects.get(pk=pk, portfolio__user=request.user)
    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            return redirect('portfolio-detail', pk=skill.portfolio.id)
    else:
        form = SkillForm(instance=skill)
    return render(request, 'portfolio/skill_form.html', {'form': form})



@login_required
def delete_skill(request, pk):
    skill = Skill.objects.get(pk=pk, portfolio__user=request.user)
    if request.method == 'POST':
        skill.delete()
        return redirect('portfolio-detail', pk=skill.portfolio.id)
    return render(request, 'portfolio/skill_confirm_delete.html', {'skill': skill})







