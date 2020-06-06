import React from 'react';

class Task extends React.Component {
    render() {
        return (
            <div>
                <input 
                    type="checkbox"
                    checked={this.props.task.done}
                    onChange={() => this.props.handleUpdate(this.props.task.id)}
                />
                <span>{this.props.task.text}</span>
            </div>
        )
    }
}

export default Task
