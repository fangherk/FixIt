import React from 'react';
import './stylesheets/AccountingBook.css';


export default class AccountingBook extends React.Component {
  state = {
    players:[
      {playerName:'A', transactions:["+23", "-45"]}, {playerName:'B', transactions:[]}, {playerName:'C', transactions:["-30"]}, {playerName:'D', transactions:["+30"]}
    ]
  };
  createTransactionEntries = (t) => {
    const rows = []
    for (let i=0; i < t.length; i++) {
      rows.push(<tr key={i} className="order-cell"><td>{t[i]}</td></tr>)
    }
    return rows

  }
  createTableColumn = () => {
    const columns = this.state.players.map(c =>  (
      <div className="Column">
        <div className="order-label"><b>{c.playerName}</b></div>
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
