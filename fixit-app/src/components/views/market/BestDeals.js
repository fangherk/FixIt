import React from 'react';
import './stylesheets/BestDeals.css';


export default class BestDeals extends React.Component {
  render() {
    return (
      <table className="bestDeals">
        <tbody>
          <tr>
            <th className="bestDeals-label">Best Bid</th>
            <th className="bestDeals-label">Best Offer</th>
          </tr>
          <tr>
            <td className="bestDeals-value">{this.props.bestBid}</td>
            <td className="bestDeals-value">{this.props.bestOffer}</td>
          </tr>
        </tbody>
      </table>
    )

  }
}
