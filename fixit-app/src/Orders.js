import React from 'react';
import './Orders.css';
import OrderRow from './OrderRow'

export default class Orders extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      value:'',
      orderType:'SELL'
    }
    this.handleOrder = this.handleOrder.bind(this);
    this.handleTextChange = this.handleTextChange.bind(this);
    this.toggleType = this.toggleType.bind(this);
    this.deleteOrder = this.props.onDelete.bind(this);
  }
  createTable() {
    let bids = this.props.bids.sort(function(a, b){return b-a});
    let offers = this.props.offers.sort(function(a, b){return a-b});

    let bid_table = [];
    let offer_table = [];
    let max_rows = Math.max(bids.length, offers.length);
    for (let i=0;i<max_rows;i++) {
      let current_bid = "\xa0";
      let current_offer = "\xa0";
      if (i < bids.length) {
        current_bid = bids[i];
      }
      if (i < offers.length) {
        current_offer = offers[i];
      }

      let bid_row = (<OrderRow key={i} value={current_bid} type="BUY" onDelete={this.deleteOrder}/>)
      let offer_row = (<OrderRow key={i} type="SELL" value={current_offer} onDelete={this.deleteOrder}/>)
      bid_table.push(bid_row);
      offer_table.push(offer_row);
    }
    return [bid_table, offer_table];
  }



  handleOrder(event) {
    if (this.state.value === "" || Number(this.state.value) < 0)  {
      event.preventDefault();
      return
    }
    this.props.onSubmit(this.state.value, this.state.orderType);

    event.preventDefault();
    this.setState({value:''});
  }

  handleTextChange(event) {
    this.setState({value: event.target.value});
  }

  toggleType(event) {
    if (this.state.orderType === "BUY") {
      this.setState({orderType:"SELL"})
    } else {
      this.setState({orderType:"BUY"})
    }
  }

  render() {
    let tables = this.createTable();
    return (
      <div className="Orders">
        <div className="Option">
          <form className="order-form" onSubmit={this.handleOrder}>
            <input type="number" placeholder="Place bid/offer" value={this.state.value} onChange={this.handleTextChange} />
          </form>
          <a className="order-button"><button className="order-button-btn"onClick={this.toggleType}>{this.state.orderType}</button></a>
        </div>
        <div className="Column">
          <div className="order-label">Bids</div>
          <table className="right">
            <tbody>
              {tables[0]}
            </tbody>
          </table>
        </div>
        <div className="Column">
          <div className="order-label">Offers</div>
          <table className="left">
            <tbody>
              {tables[1]}
            </tbody>
          </table>
        </div>
      </div>
    )
  }
}
