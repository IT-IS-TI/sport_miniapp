import React, {useState} from "react"
import './ProgressBar.css'

const ProgressBar = (props) => {
  
  //console.log(props);

  let progress = 0;
  let measurableProgress = 0;
  let need;
  if(props.type == "Sport hours") {
    progress = props.hours / (props.needHours / 100);
    measurableProgress = props.hours;
    need = props.needHours;
  } else if (props.type == "Sport points") {
    progress = props.points / (props.needPoints / 100);
    measurableProgress = props.points;
    need = props.needPoints;
  } else if (props.type == "Challenge Bar") {
    progress = props.actual / (props.need / 100);
    measurableProgress = props.actual;
    need = props.need;
  } else {
    console.log("bad bar type recognission");
  }

  const getColor = () => {
    if(progress < 40) {
      return "#ff0000";
    } else if (progress < 70) {
      return "#ffa500";
    } else {
      return "#2ecc71";
    }
  }

  return (
    <div className="container">
      <div className="bar-name">{props.name}</div>
      <div className={"description"}>{props.description}</div>
      <div className="progress-bar">
         <div data-testid="fill-bar"  className="progress-bar-fill" style={{ width: `${progress}%`, backgroundColor: getColor()}}>{measurableProgress}/{need}</div>
      </div>
    </div>
  )
};

export default ProgressBar;



