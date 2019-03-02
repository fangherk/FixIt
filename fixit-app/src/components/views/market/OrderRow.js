import React from 'react';
import './stylesheets/OrderRow.css';

export default class OrderRow extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      lastPress:0
    }
    this.handleClick = this.handleClick.bind(this);
  }
  componentDidMount() {
    document.addEventListener('click', this.handleClick);
  }

  componentWillUnmount() {
    document.removeEventListener('click', this.handleClick);

  }
  handleClick(event) {
    //detects double tap on order
    if (this.node.contains(event.target)) {
      let delta = new Date().getTime() - this.state.lastPress;

      if(delta < 200) {
        //double tap happened
        this.props.onDelete(this.props.value, this.props.type)

        event.preventDefault();
        return;
      }

      this.setState({
        lastPress: new Date().getTime()
      })
    }
  }

  render() {
    return (
      <tr key={this.key}
          value={this.props.value}
          className="order-cell"
          ref={node => this.node = node}>

        <td>{this.props.value}</td>
      </tr>

    )
  }
}
