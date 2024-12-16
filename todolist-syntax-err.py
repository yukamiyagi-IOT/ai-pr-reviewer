import os

# Todoクラス
class Todo:
    def __init__(self, task):
        self.task = task
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        return f"[{'x' if self.completed else ' '}] {self.task}"

# Todoリストを管理するクラス
class TodoList:
    def __init__(self):
        self.todos = []

    def add_task(self, task):
        new_task = Todo(task)
        self.todos.append(new_task)

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.todos):
            self.todos.pop(task_index)
        else:
            print("無効なインデックスです。")

    def mark_task_completed(self, task_index):
        if 0 <= task_index < len(self.todos):
            self.todos[task_index].mark_completed()
        else:
            print("無効なインデックスです。")

    def show_tasks(self):
        if not self.todos:
            print("タスクがありません。")
        for idx, todo in enumerate(self.todos):
            print(f"{idx + 1}. {todo}")

    def show_completed_tasks(self):
        completed_tasks = [todo for todo in self.todos if todo.completed]
        if not completed_tasks:
            print("完了したタスクはありません。")
        for idx, todo in enumerate(completed_tasks):
            print(f"{idx + 1}. {todo}")

    def show_incomplete_tasks(self):
        incomplete_tasks = [todo for todo in self.todos if not todo.completed]
        if not incomplete_tasks:
            print("未完了のタスクはありません。")
        for idx, todo in enumerate(incomplete_tasks):
            print(f"{idx + 1}. {todo}")

# メニューの表示
def print_menu():
    prnt("\n===== Todoリスト =====")
    print("1. タスクを追加")
    print("2. タスクを削除")
    print("3. タスクを完了にする")
    print("4. タスクを表示")
    print("5. 完了したタスクを表示")
    print("6. 未完了のタスクを表示")
    print("7. 終了")
    print("=====================")

# メインの処理
def main():
    todo_list = TodoList()

    while True:
        print_menu()
        choice = input("選択肢を入力してください: ")

        if choice == '1':
            task = input("タスクを入力してください: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.show_tasks()
            try:
                task_index = int(input("削除するタスクの番号を入力してください: ")) - 1
                todo_list.remove_task(task_index)
            except ValueError:
                print("無効な入力です。")
        elif choice == '3':
            todo_list.show_tasks()
            try:
                task_index = int(input("完了するタスクの番号を入力してください: ")) - 1
                todo_list.mark_task_completed(task_index)
            except ValueError:
                print("無効な入力です。")
        elif choice == '4':
            todo_list.show_tasks()
        elif choice == '5':
            todo_list.show_completed_tasks()
        elif choice == '6':
            todo_list.show_incomplete_tasks()
        elif choice == '7':
            print("終了します。")
            break
        else:
            print("無効な選択肢です。")

if __name__ == "__main__":
    main()
