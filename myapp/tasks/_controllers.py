from flask import render_template, request, redirect, url_for
from flask.views import View

from myapp import app

task_list = ['task 1','task 2','task 3']

class ListView(View):
    init_every_request = False

    def __init__(self, template) -> None:
        self.template = template  

    def dispatch_request(self):
        tasks=task_list
        return render_template(self.template, tasks=tasks)    
    
app.add_url_rule('/tasks/', view_func=ListView.as_view('tasks.list', 'dashboard/task/index.html'))


class CreateView(View):
    methods = ['GET', 'POST']    
    init_every_request = False

    def __init__(self, template) -> None:
        self.template = template

    def dispatch_request(self):
        task = request.form.get("task_input")
        if task is not None:
            task_list.append(task)
            return redirect(url_for('tasks.index'))

        return render_template(self.template)


class UpdateView(View):
    methods = ['GET', 'POST']
    init_every_request = False

    def __init__(self, template) -> None:
        self.template = template

    def dispatch_request(self, id):
        task = request.form.get("task_input")
        if task is not None:
            task_list[id] = task
            return redirect(url_for('tasks.index'))

        return render_template(self.template)
    
class DeleteView(View):
    init_every_request = False

    def __init__(self) -> None:
        pass

    def dispatch_request(self, id):
        del task_list[id]    
        return redirect(url_for('tasks.index'))
     
app.add_url_rule('/tasks/', view_func=ListView.as_view('tasks.index', 'dashboard/task/index.html'))
app.add_url_rule('/tasks/create', view_func=CreateView.as_view('tasks.create', 'dashboard/task/create.html'))
app.add_url_rule('/tasks/update/<int:id>', view_func=UpdateView.as_view('tasks.update', 'dashboard/task/update.html'))
app.add_url_rule('/tasks/delete/<int:id>', view_func=DeleteView.as_view('tasks.delete'))