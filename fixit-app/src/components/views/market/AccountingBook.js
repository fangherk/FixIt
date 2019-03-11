import React from 'react';
import './stylesheets/AccountingBook.css';


export default class AccountingBook extends React.Component {
  createTransactionEntries = (t) => {
    let rows = []
    for (let i=0; i < t.length; i++) {
      rows.push(<tr key={i} className="order-cell"><td key={i} >{t[i]}</td></tr>)
    }
    return rows

  }
  createTableColumn = () => {
    const columns = this.props.accounting.map(c =>  (
      <div className="Column" >
        <div className="order-label"><b>{c.player}</b></div>
        <table className="left">
          <tbody>
            {this.createTransactionEntries(c.transactions)}
          </tbody>
        </table>
      </div> )
    );
    return columns
  }
  render() {

    return (
    <div className = 'AccountingBook'>
    <div className='title' style = {{fontWeight:'bold', fontSize:25}} >
          <p>Accounting Book</p>
    </div>
    <div className="row">
      {this.createTableColumn()}
      </div>
    </div>
    );
  }
}
