import React from 'react';

class Filter extends React.Component {
    render() {
        return (
            <div>
                <input 
                    type="checkbox"
                    checked={this.props.hideDoneTask}
                    onChange={() => this.props.handleFilterTasks()}
                />
                <span>hide completed</span>
            </div>
        )
    }
}

export default Filter
