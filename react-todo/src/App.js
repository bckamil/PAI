import React from 'react';
import './App.css';

import Filter from './components/Filter'
import NewTask from './components/NewTask'
import ToDoList from './components/ToDoList'

class App extends React.Component {
  constructor() {
    super()
    this.state = {
      hideDoneTask: false,
      todos: []
    }
    this.handleAddTask = this.handleAddTask.bind(this);
    this.handleFilterTasks = this.handleFilterTasks.bind(this);
    this.handleUpdate = this.handleUpdate.bind(this);
  }

  handleFilterTasks() {
    this.setState(prevState => ({
      hideDoneTask: !prevState.hideDoneTask
    }))
  }
  handleAddTask(text) {
    console.log(text)
    if (text.length > 0) {
      console.log('XD')
      let newTask = {
        id: this.state.todos.length + 1,
        done: false,
        text: text
      }
      let todos = this.state.todos;
      todos.push(newTask);
      this.setState({ todos })
    }
  }
  handleUpdate(id) {
    let todos = this.state.todos;
    const position = todos.map(function (e) { return e.id; }).indexOf(id);
    todos[position].done = !todos[position].done;
    this.setState({ todos });
  }

  render() {
    let todos = this.state.todos
    if (this.state.hideDoneTask) {
      todos = todos.filter(task => !task.done)
    }
    let todoListHtml
    if (todos.length > 0) {
      todoListHtml = <ToDoList tasks={todos} handleUpdate={this.handleUpdate} />
    } else {
      todoListHtml = <h4>No data to show</h4>
    }

    return (
      <div className="todo-app">
        <Filter handleFilterTasks={this.handleFilterTasks} />
        <hr />
        {todoListHtml}
        <hr />
        <NewTask handleAddTask={this.handleAddTask} />
      </div>
    )
  }
}

export default App;
