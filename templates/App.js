import React from 'react';
import ReactDOM from 'react-dom';
import jQuery from 'jquery';


class App extends React.Component {
  constructor() {
    super();
    var self = this;
    this.state = {data: [] };
    this.onDataReceived = this.onDataReceived.bind(this);
  }



  onDataReceived(data) {
    console.log("data received");
    console.log(data);
    this.setState({data: data});
  }

  componentWillMount() {
    console.log('mounted!!!!!');
  }
  componentDidMount() {
    jQuery.get( "http://localhost:5000/data", function(data) {
      this.onDataReceived(data.data);
    }.bind(this));
  }

  render(){
    return (<div>
     { this.state.data.map(function(item) {
        return (<div>
                  {item.title}
                </div>)
         })
     }
     </div>);
  }
}



export default App
