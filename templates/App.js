import React from 'react';
import ReactDOM from 'react-dom';
import jQuery from 'jquery';
import moment from 'moment';


class App extends React.Component {
  constructor() {
    super();
    var self = this;
    this.state = {data: [] };
    this.onDataReceived = this.onDataReceived.bind(this);
  }

  onDataReceived(data) {
    this.setState({data: data});
  }

  componentDidMount() {
    jQuery.get( "http://localhost:5000/data", function(data) {
      this.onDataReceived(data.data);
      console.log(data.data);
    }.bind(this));
  }

  render(){
    var getDaysSincePublished = function(day) {
      var days = moment().diff(moment(day), 'days');
      var diff;
      if (days == 0)
        diff = moment().diff(moment(day), 'hours').toString() + "h ago";
      else
        diff = days.toString() + "d ago";
      return diff;
    }
    return (<div>
     { this.state.data.map(function(item) {
        return (<div className="job">
                  <div className="logo-col">
                    <Img src={"https://logo.clearbit.com/" + item.logo + ".com"}/>
                  </div>
                  <div className="first-col">
                    <div className="title">
                      {item.title}
                    </div>
                    <div className="company">
                      {item.company}
                    </div>
                  </div>
                  <div className="second-col">
                    <div className="tags">
                      tags
                    </div>
                  </div>
                  <div className="third-col">
                    <div className="location">
                      <i className="fa fa-map-marker"></i>
                      {item.location}
                    </div>
                    <div className="published">
                      {getDaysSincePublished(item.published)}
                    </div>
                  </div>
                </div>)
         })
     }
     </div>);
  }
}

class Img extends React.Component {
  constructor() {
    super();
    this.fixImages = this.fixImages.bind(this);

  }
  componentWillMount() {
    this.state = {source: this.props.src};
  }

  fixImages() {
    this.setState( { source: "https://logo.clearbit.com/criteo.com" });
  }

  render() {
    return <img src={this.state.source} onError={this.fixImages}/>
  }
}



export default App
