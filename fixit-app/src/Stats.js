import React from 'react';
import './Stats.css';


export default class Stats extends React.Component {
  createTable = () => {
    let table = [];
    let stats = this.props.stats;

    for (let i=0; i < stats.length; i++) {
      let current_stat = stats[i];
      let stat_row = (
      <tr key={i}>
        <td className="stat-name"><b>{current_stat[0]} : </b></td>
        <td className="stat-value">{current_stat[1]}</td>
      </tr>
      )
      table.push(stat_row);

    }

    return table;
  }

  render() {
    return (
      <table className="Stats">
        <tbody>
          {this.createTable()}
        </tbody>
      </table>
    )
  }
}
