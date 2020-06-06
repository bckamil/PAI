import React from 'react';
import Task from './Task';

class ToDoList extends React.Component {
    render() {
        return (
            <div>
                {this.props.tasks.map((task, i) => <Task task={task} key={i} handleUpdate={this.props.handleUpdate} />)}
            </div>
        )
    }
}

export default ToDoList
