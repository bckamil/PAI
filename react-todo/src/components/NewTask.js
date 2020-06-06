import React from 'react';

class NewTask extends React.Component {
  constructor() {
    super()
    this.state = {
      text: ''
    }
    this.updateTextValue = this.updateTextValue.bind(this);
    this.addTask = this.addTask.bind(this);
  }
  render() {
    return (
      <div>
        <input type="text" value={this.state.text} onChange={this.updateTextValue} />
        <button onClick={this.addTask}>Add</button>
      </div>
    )
  }
  updateTextValue(evt) {
    this.setState({
      text: evt.target.value
    });
  }
  addTask() {
    this.props.handleAddTask(this.state.text);
    this.setState({
      text: ''
    })
  }
}

export default NewTask
