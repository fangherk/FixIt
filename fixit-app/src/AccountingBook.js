import React from 'react';
import './AccountingBook.css';


export default class AccountingBook extends React.Component {
  state = {
    players:[
      {playerName:'A', transactions:["+23", "-45"]}, {playerName:'B', transactions:[]}, {playerName:'C', transactions:["-30"]}, {playerName:'D', transactions:["+30"]}
    ]
  };
  createTransactionEntries = (t) => {
    const rows = []
    for (let i=0; i < t.length; i++) {
      rows.push(<tr className="order-cell"> {t[i]} </tr>)
    }
    return rows

  }
  createTableColumn = () => {
    const columns = this.state.players.map(c =>  (
      <div className="Column">
        <div className="order-label"><b>{c.playerName}</b></div>
            <table className="left">
              {this.createTransactionEntries(c.transactions)}
          </table>
        </div> )
      );
    return columns
  }
  render() {

    return (
    <div className = 'AccountingBook'>
    <div className='title' style = {{fontWeight:'bold', fontSize:25}} >
          <p>  Accounting Book</p>
    </div>
    <div class="row">
      {this.createTableColumn()}
      </div>
    </div>
    );
  }
}
