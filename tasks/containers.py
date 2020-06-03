class TaskList:
    def __init__(self, columns=None):
        if columns is None:
            self.columns = [Column('To Do'), Column('In Progress'), Column('Complete')]
        else:
            columns = columns


class Column:
    def __init__(self, name, tasks=None):
        self.name = name
        if self.tasks is None:
            self.tasks = {}
        else
            self.tasks = tasks


class Task:
    def __init__(self, name, task_list=None):
        self.name = task_name
        self.task_list = task_list
